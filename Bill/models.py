from django.db import models
from Client.models import Client


# Create your models here.
class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=False)
    nit = models.IntegerField(unique=True)
    code = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.id} - {self.company_name} {self.nit}"

    class Meta:
        ordering = ["id"]

    def natural_key(self):
        return ({"id": self.id, "company_name": self.company_name, "nit": self.nit, "code": self.code, "client_id": self.client_id.natural_key()})
    natural_key.dependencies = ['API.Clients']
    objects = models.Manager()
