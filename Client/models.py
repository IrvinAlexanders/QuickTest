from django.db import models


# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"

    def natural_key(self):
        return ({"id": self.id, "document": self.document, "first_name": self.first_name, "last_name": self.last_name, "email": self.email})
    objects = models.Manager()
