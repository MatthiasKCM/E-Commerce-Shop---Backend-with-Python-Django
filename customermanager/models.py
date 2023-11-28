from django.db import models
from django.db.models import CharField


# Create your models here.

class Customer(models.Model):
    #Instanzvariablen:
    salutation = CharField(max_length=5)
    surname = CharField(max_length=20)
    last_name = CharField(max_length=30)
    birthday = models.DateField()
    password = CharField(max_length=15)
    email = CharField(max_length=10)

    def __str__(self):
        return(
            f"Anrede: {self.salutation}<br> "
               f"Vorname: {self.surname}<br> "
               f"Nachname: {self.last_name}<br> "
               f"Geburtstag: {self.birthday}<br> "
               f"Passwort: {self.password}<br> "
               f"Email: {self.email}")



