from django.http import JsonResponse, HttpResponse
import json
from .models import Client
from django.core.serializers import serialize
from Bill.models import Bill
import csv, io
from django.shortcuts import render
from django.contrib import messages
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
    lookup_field = 'pk'

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

def export(request):
    
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['document','First Name', 'Last Name', 'Email', 'Bill Id', 'Company name'])
    
    data_client = Client.objects.all()
    data_bills = Bill.objects.all()
    print(data_client)
    for cli in data_client:
        for bil in data_bills:
            if bil.client_id_id == cli.id:
                id_bil = bil.id
                company_name = bil.company_name
                client = [cli.document,cli.first_name, cli.last_name, cli.email, id_bil , company_name]
                writer.writerow(client)

    response['Content-Disposition'] = 'attachment; filename="clients.csv"'

    return response



def upload_csv(request):
    template = "clients/upload.html"
    prompt ={
        'order' : 'Order of the CSV should be document, first_name, last_name, email'
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Client.objects.update_or_create(
            id = column[0],
            document = column[1],
            first_name = column[2],
            last_name = column[3],
            email = column[4]
        )
    context={}
    return render(request, template, context)

