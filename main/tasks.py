import pandas as pd
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@shared_task
def parse_cv(args):
    print("inside")
    sales_sum = 0
    quantity_sum = 0
    discount_sum = 0
    profit_sum = 0
    sales_avg = 0
    quantity_avg = 0
    discount_avg = 0
    profit_avg = 0
    for row in args["csv_data"]:
        if not len(row) > 4:
            continue
        if isinstance(row[1], int) or isinstance(row[1], float):
            sales_sum += row[1]
        if isinstance(row[2], int) or isinstance(row[2], float):
            quantity_sum += row[2]
        if isinstance(row[3], int) or isinstance(row[3], float):
            discount_sum += row[3]
        if isinstance(row[4], int) or isinstance(row[4], float):
            profit_sum += row[4]
    
    if len(args["csv_data"]) != 0:
        sales_avg = round(sales_sum / len(args["csv_data"]))
        quantity_avg = round(quantity_sum / len(args["csv_data"]))
        discount_avg = round(discount_sum / len(args["csv_data"]))
        profit_avg = round(profit_sum / len(args["csv_data"]))
    calculation_data = {
        "sales_sum" : round(sales_sum),
        "quantity_sum" : round(quantity_sum),
        "discount_sum" : round(discount_sum),
        "profit_sum" : round(profit_sum),
        "sales_avg" : round(sales_avg),
        "quantity_avg" : round(quantity_avg),
        "discount_avg" : round(discount_avg),
        "profit_avg" : round(profit_avg),
    }
    channel_layer = get_channel_layer()
    broadcast_data = {
        "type" : "csv_data",
        "data" : args["csv_data"],
        "calculation_data" : calculation_data
    }
    print(broadcast_data)
    async_to_sync(channel_layer.group_send)(
            f"csv_data_{args['layer_id']}",
            broadcast_data
    )