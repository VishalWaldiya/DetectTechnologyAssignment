from django.test import TestCase
import datetime
from account.models import EmployeeDetail

class EmployeeDetailTestCase(TestCase):
    def setUp(self):
        EmployeeDetail.objects.create(
            employeeId = "100",
            designation = "Developer",
            date_of_joining = datetime.date(2020,3,5),
            name = "Vishal",
            address = "Chennai",
            phone_number = "+916363153725",
            email = "vishalwaldiya@gmail.com"
        )

    def test_EmployeeDetails_are_not_duplicated(self):
        """EmployeeDetails repeated or not"""
        obj,created = EmployeeDetail.objects.get_or_create(
            employeeId = "100",
            designation = "Developer",
            date_of_joining = datetime.date(2020,3,5),
            name = "Vishal",
            address = "Chennai",
            phone_number = "+916363153725",
            email = "vishalwaldiya@gmail.com"
        )

        if created:
            print("Values Being Duplicated")
        else:
            print("value Already Exists")