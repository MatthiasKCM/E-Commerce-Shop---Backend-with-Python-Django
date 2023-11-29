from django.shortcuts import render,get_object_or_404,HttpResponse

from cartmanager.models import Cart, Entry


# Create your views here.

def show_cart(request, id):
    cart = get_object_or_404(Cart, id=id)
    entries = cart.entry_set.all() #cart.entry_set wird automatisch bei einer Relation von Django erstellt, kann auf alle Objekte zugreifen die mit cart verknüpft sind
    total_price = cart.calaculate_total_price()
    surname_customer = cart.get_surname_customer()
    print(f" Hallo {surname_customer} hier ist dein Warenkorb: \n ------------------------------------------")
    for entry in entries:
        print(f" {entry}\n ------------------------------------------")

    print(f" Warenkorb Gesamtbrutto: {total_price} Euro\n")
    return HttpResponse("Cart und Entries in der Konsole ausgegeben.")
