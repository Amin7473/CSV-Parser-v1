import json
from channels.generic.websocket import WebsocketConsumer
from urllib.parse import parse_qs 
from asgiref.sync import async_to_sync


class CSVLayerConsumer(WebsocketConsumer):
    """Consumer for getting task list"""

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.conversation_name = None

    def connect(self):
        self.accept()
        try:
            query_string_bytes = self.scope.get("query_string", b"")
            query_string = parse_qs(query_string_bytes.decode("utf-8"))
            print(query_string)
            layer_id = query_string["layer_id"][0]
            self.conversation_name = f"csv_data_{str(layer_id)}"
            print(self.conversation_name)

            async_to_sync(self.channel_layer.group_add)(
                self.conversation_name,
                self.channel_name,
            )

        except Exception as e:
            self.api_logger.info(f"Task List Socket was disconnected due to , {str(e)}")
            self.disconnect(close_code=f"Task List Socket was disconnected due to , {str(e)}")

    def csv_data(self, event):
        self.send(text_data=json.dumps(event))