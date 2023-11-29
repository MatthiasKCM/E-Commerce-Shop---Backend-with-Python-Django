from django.shortcuts import render, get_object_or_404,HttpResponse
from addressmanager.models import Address


# Create your views here.

def show_address_by_id(request, id):
    address = get_object_or_404(Address, pk=id)
    return HttpResponse(f"Kundenaddresse: <br> {address}")

def show_all_addresses_by_id(request,id):
    addresses = Address.objects.filter(id__gte=id) # ODER get_list_or_404(Address,id__gte=id)
    return_value = ''
    for ad in addresses:
        return_value += f"{ad} "
    return HttpResponse(return_value)