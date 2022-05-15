from django.db import models
from Bill.models import Bill
from Product.models import Product


# Create your models here.

class BillsProduct(models.Model):

    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.bill_id} {self.product_id}"

    class Meta:
        ordering = ["id"]

    def natural_key(self):
        return ({"id": self.id, "bill_id": self.bill_id, "product_id": self.product_id})
    objects = models.Manager()