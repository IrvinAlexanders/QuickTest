from django.db import models


# Create your models here.
class Product(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    attribute = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.id} - {self.name} {self.description}"
    objects = models.Manager()

    def natural_key(self):
        return ({"id": self.id, "name": self.name, "description": self.description})