from django.contrib import admin
from .models import User #Del archivo model importamos la clase User


# Register your models here.
admin.site.register(User) #El modelo se registra en el administrador