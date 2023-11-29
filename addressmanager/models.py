from django.db import models

from customermanager.models import Customer


# Create your models here.
class Address(models.Model):
    GENDER_CHOICES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.street} {self.house_number}, {self.postal_code} {self.city}"