from django.shortcuts import render,HttpResponse, get_object_or_404, get_list_or_404
from customermanager.models import Customer


# Create your views here.
def show_customer(request):
    return HttpResponse('Hier ist dein Kunde.')


def show_customer_details(request,id):
    customer = Customer.objects.get(id=id)
    addresses = customer.address_set.all()
    for address in addresses:
        print(f"{address}\n-------------")
    return HttpResponse(f"Hier sind die Kundendetails mit der ID: {id}")


def show_first_customer(request):
    customer = Customer.objects.first()
    return HttpResponse(f"Vorname: {customer.surname}")

def write_customer(request):
    customer = Customer(salutation="Frau",surname="Matthias",last_name="Popp", birthday= "1999-01-05", password= "niki123",email="bla@gmail.com")
    customer.save() # speichert Daten in Datenbank
    customer = Customer.objects.last() #letzte Objekt bekommen
    return HttpResponse(f"Geschriebene Kundendaten: <br> {customer}")