from django.db import models

from customermanager.models import Customer


# Create your models here.

class Cart(models.Model):
    cart_net_total = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE, null=True) #1:1 Beziehung, True heisst das ein cart optional ist

    def calaculate_total_price(self):
        entries = self.entry_set.all()
        total_price = sum(entry.gross_total for entry in entries) #iteriert durch QuerySet und rechnet einzelne Preise zusammen
        return total_price

    def get_surname_customer(self):
        surname = self.customer.surname
        return surname

    def __str__(self):
        return (f"Warenkorb netto: {self.cart_net_total}</br>"
                f"Steuer: {self.tax_amount}</br>"
                f"Warenkorb brutto:  {self.cart_gross_total}</br>")

class Entry(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE) # CASCADE lóscht in dem Fall auch alle zugehórigen entries
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    net_value_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    gross_value_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    gross_total = models.DecimalField(max_digits=10, decimal_places=2)
    net_total = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Entry ID: {self.id}, Product: {self.product_name}, Quantity: {self.quantity}, Gross Total: {self.gross_total}"
