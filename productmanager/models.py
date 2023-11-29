from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    product_number = models.CharField(max_length=20, unique=True)
    price_brutto = models.DecimalField(max_digits=10, decimal_places=2)
    price_netto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return mark_safe(f"Produktname: {self.name}<br>"
                         f"Produktnummer: {self.product_number}<br>"
                         f"Bruttopreis: {self.price_brutto}<br>"
                         f"Nettopreis: {self.price_netto}")
