from django.contrib import admin
from customermanager.models import Customer


# Register your models here.

class AdminCustomer(admin.ModelAdmin):
    list_display = ["surname","last_name","email", "display_password_strength"]
    fieldsets = [
        ("Basisdaten",{"fields":["surname","last_name","email"]}),
        ("Kundendetails",{"fields":["salutation","birthday","password"]})
    ]

    def display_password_strength(self,obj):
        if len(obj.password)>2:
            return True
        else:
            return False

    display_password_strength.short_description = "Passwortsicherheit"
    display_password_strength.boolean = True


admin.site.register(Customer,AdminCustomer)