from rest_framework import serializers
from .models import Bill, BillsProduct
from Product.models import Product



class BillProductsSerializer(serializers.ModelSerializer):

    bill = serializers.CharField()
    products = serializers.CharField()

    class Meta:
        model = BillsProduct
        fields = ['id', 'bill_id', 'products_id']

    def create(self, data):

        new_bill = Bill.objects.filter(pk=data['bill']).first()
        new_product = Product.objects.filter(pk=data['products']).first()

        new_bill_product = BillsProduct.objects.create(
            products=new_product,
            bill=new_bill
        )
        return new_bill_product