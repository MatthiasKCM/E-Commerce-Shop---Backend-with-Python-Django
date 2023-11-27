from django.shortcuts import render,HttpResponse, get_object_or_404, get_list_or_404
from customermanager.models import Customer


# Create your views here.
def show_customer(request):
    return HttpResponse('Hier ist dein Kunde.')


def show_customer_details(request,id):
    customers = get_object_or_404(Customer, pk=id)
    return HttpResponse(customers)