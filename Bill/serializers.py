from rest_framework import serializers
from .models import Bill


class BillModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ('company_name', 'nit', 'code', 'client_id')

