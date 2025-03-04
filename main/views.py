import uuid
import pandas as pd
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from main.tasks import parse_cv
# Create your views here.
def home_page(request):
    layer_id = str(uuid.uuid4())
    return render(request, "index.html", context={"layer_id" : layer_id})

@api_view(['POST'])
def upload_csv(request):
    if request.method == "POST":
        file = request.FILES['csv_file']
        print(file.name)
        df = pd.read_csv(file)
        print(df.columns)
        mandatory_columns = ["Product Name", "Sales", "Quantity", "Discount", "Profit"]
        columns = list(df.columns)
        if not all(col in columns for col in mandatory_columns):
            return Response("Invalid CSV File Format. Use the given template", status=status.HTTP_400_BAD_REQUEST)
        data_dict = df.values.tolist()
        print(1)
        parse_cv({
            "layer_id" : request.data.dict()["layer_id"],
            "csv_data" : data_dict
        })
        print(2)
        
        return Response({"message" : "CSV Parsing started..."}, status=status.HTTP_200_OK)