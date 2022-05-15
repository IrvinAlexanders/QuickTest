from django.http import JsonResponse
from django.views.generic import View
import json
from Bill.models import Bill
from .models import BillsProduct
from Product.models import Product
from django.core.serializers import serialize
from .serializers import BillProductsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 


class BillsProductView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = BillProductsSerializer

    def get(self, request, pk=None):
        if pk == None:
            queryset = BillsProduct.objects.all().order_by("id").select_related()
        else:
            queryset = BillsProduct.objects.filter(id=pk).select_related()

        name = queryset.model.__name__
        bill_product = json.loads(
            serialize("json", queryset, use_natural_foreign_keys=True))
        dataJSON = {name: bill_product}
        return JsonResponse(dataJSON, safe=True, status=200)

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        data["bill_id"] = Bill.objects.get(id=data["bill_id"])
        data["product_id"] = Product.objects.get(id=data["product_id"])
        bill_product, created = BillsProduct.objects.get_or_create(**data)
        message = "Bill Products created successfully."
        data = {"message": message, "Bill_Product_id": bill_product.id}
        return JsonResponse(data=data, safe=True, status=200)