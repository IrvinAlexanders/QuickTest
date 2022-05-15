from django.http import JsonResponse
import json
from .models import Product
from django.core.serializers import serialize
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductModelSerializer



class ProductView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ProductModelSerializer

    def get(self, request, pk=None):
        if pk == None:
            queryset = Product.objects.all().order_by("id")
        else:
            queryset = Product.objects.filter(id=pk)
        name = queryset.model.__name__
        product = json.loads(serialize("json", queryset))
        dataJSON = {name: product}
        return JsonResponse(dataJSON, safe=True, status=200)

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        product, created = Product.objects.get_or_create(**data)
        message = "Products created successfully."
        data = {"message": message, "Product_id": product.id}
        return JsonResponse(data=data, safe=True, status=200)

    def put(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        data_dict = data["fields"]
        Product.objects.filter(id=pk).update(**data_dict)

        products_data = Product.objects.filter(id=pk)
        product = json.loads(serialize("json", products_data))

        message = "Products Updated successfully."
        data = {"message": message, products_data.model.__name__: product}
        return JsonResponse(data=data, safe=True, status=200)

    def delete(self, request, pk=None):
        queryset = Product.objects.filter(id=pk)
        name = queryset.model.__name__
        bill = json.loads(serialize("json", queryset))

        Product.objects.filter(id=pk).delete()

        message = "Products deleted succesfully."
        data = {"message": message, name: bill}
        return JsonResponse(data=data, safe=True, status=200)