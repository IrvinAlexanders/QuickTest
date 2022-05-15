from django.contrib import admin
from django.urls import URLPattern, path, include
from django.db import router
from Client.views import *
from Bill.views import *
from BillsProduct.views import*
from Product.views import *
from rest_framework import routers
from User.views import *



router = routers.DefaultRouter()
router.register('bills', BillView, basename='Bill')
router.register('client', ClientView, basename='Client')
router.register('products', ProductView, basename='Product')
router.register('bills_products', BillsProductView, basename='BillsProduct')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('export/', export),
    path('import/', upload_csv)
]

