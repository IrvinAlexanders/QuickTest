from django.http import JsonResponse, HttpResponse
import json
from .models import Client
from django.core.serializers import serialize
import sqlite3
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ClientModelSerializer


db_path = settings.DATABASES['default']['NAME']
# Create your views here.
class ClientView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ClientModelSerializer
    queryset = Client.objects.all()
    lookup_field = 'id'

    def get(self, request, pk=None):
        if pk == None:
            queryset = Client.objects.all().order_by("id")
        else:
            queryset = Client.objects.filter(id=pk)
        name = queryset.model.__name__
        client = json.loads(serialize("json", queryset))
        dataJSON = {name: client}
        return JsonResponse(dataJSON, safe=True, status=200)

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        client, created = Client.objects.get_or_create(**data)
        message = "Client created successfully."
        data = {"message": message, "client_id": client.id}
        return JsonResponse(data=data, safe=True, status=200)

    def put(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        data_dict = data["fields"]
        Client.objects.filter(id=pk).update(**data_dict)

        client_data = Client.objects.filter(id=pk)
        client = json.loads(serialize("json", client_data))

        message = "Client Updated successfully."
        data = {"message": message, client_data.model.__name__: client}
        return JsonResponse(data=data, safe=True, status=200)

    def delete(self, request, pk=None):
        queryset = Client.objects.filter(id=pk)
        name = queryset.model.__name__
        client = json.loads(serialize("json", queryset))

        Client.objects.filter(id=pk).delete()

        message = "Client deleted succesfully."
        data = {"message": message, name: client}
        return JsonResponse(data=data, safe=True, status=200)

@csrf_exempt
def exportFile(request):

    if request.method == 'GET':
        conn = sqlite3.connect(str(db_path))
        query_clients = conn.execute("SELECT * from API_clients")

        data = []
        for row in query_clients:
            query_bills = conn.execute(
                "select * from API_bills where client_id_id = ?", (row[0],))
            query_bills = query_bills.fetchall()
            data.append({
                "document": row[1],
                "full_name": f'{row[2]} {row[3]}',
                "bills": len(query_bills),
            })
        csv_object = pd.DataFrame.from_dict(data)

        file = csv_object.to_csv(index=None)
        response = HttpResponse(file, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=QuickTest.csv'
        return response


@csrf_exempt
def importFile(request):

    if request.method == 'POST':
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        registries = "INSERT INTO API_clients (document, first_name, last_name, email) VALUES(?, ?, ?, ?)"
        csv_file = request.FILES["csv_file"]
        file_data = csv_file.read().decode("utf-8")

        file_data = [data.split(",") for data in file_data.split("\r\n")]
        del file_data[0]
        try:
            data_to_import = [(row[0], row[1], row[2], row[3])
                              for row in file_data]
            cursor.executemany(registries, data_to_import)
            conn.commit()
        except:
            return JsonResponse({"message": "error al importar archivo"}, status=400)
        return JsonResponse({"data": file_data}, safe=True, status=200)

