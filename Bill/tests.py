from django.test import TestCase
from .models import Bill


# Create your tests here.
class BillTestCase(TestCase):

    def setUp(self):
        Bill.objects.create(client_id=4, company_name="KFC", nit=10230010, code="kfc-20220515")
        Bill.objects.create(client_id=4, company_name="KFC", nit=10230010, code="kfc-20220516")
        