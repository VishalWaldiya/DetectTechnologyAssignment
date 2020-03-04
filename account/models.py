from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class EmployeeDetail(models.Model):
    """Model definition for EmployeeDetail."""

    employeeId = models.BigIntegerField()
    designation = models.CharField(blank=True, max_length=500)
    date_of_joining = models.DateField(blank=True, auto_now=False, auto_now_add=False)
    name = models.CharField(blank=True, max_length=500)
    address = models.TextField(blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True, max_length=254)

    class Meta:
        """Meta definition for EmployeeDetail."""

        verbose_name = 'EmployeeDetail'
        verbose_name_plural = 'EmployeeDetails'
        unique_together = ['employeeId','designation','date_of_joining','name','address','phone_number','email']

    def __str__(self):
        """Unicode representation of EmployeeDetail."""
        return '{}'.format(self.name ) # TODO

    # def save(self):
    #     """Save method for EmployeeDetail."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for EmployeeDetail."""
    #     return ('')
