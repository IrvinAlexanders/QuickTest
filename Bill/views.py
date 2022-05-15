from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
import json
from .serializers import BillModelSerializer
from .models import Bill
from Client.models import Client
from django.core.serializers import serialize



# Create your views here.
class BillView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = BillModelSerializer
    queryset = Bill.objects.all()
    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk == None:
            queryset = Bill.objects.all().order_by("id").select_related()
        else:
            print("sadasd")
            queryset = Bill.objects.filter(id=pk).select_related()
        name = queryset.model.__name__
        bill = json.loads(serialize("json", queryset,
                          use_natural_foreign_keys=True))
        dataJSON = {name: bill}
        return JsonResponse(dataJSON, safe=True, status=200)

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        pk = data["client_id"]
        data["client_id"] = Client.objects.get(id=pk)
        bill, created = Bill.objects.get_or_create(**data)
        message = "Bill created successfully."
        data = {"message": message, "Bill_id": bill.id}
        return JsonResponse(data=data, safe=True, status=200)

    def put(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        data_dict = data["fields"]
        Bill.objects.filter(id=pk).update(**data_dict)

        bill_data = Bill.objects.filter(id=pk)
        bill = json.loads(serialize("json", bill_data))

        message = "Bills Updated successfully."
        data = {"message": message, bill_data.model.__name__: bill}
        return JsonResponse(data=data, safe=True, status=200)

    def delete(self, request, pk=None):
        queryset = Bill.objects.filter(id=pk)
        name = queryset.model.__name__
        bill = json.loads(serialize("json", queryset))

        Bill.objects.filter(id=pk).delete()

        message = "Bills deleted succesfully."
        data = {"message": message, name: bill}
        return JsonResponse(data=data, safe=True, status=200)