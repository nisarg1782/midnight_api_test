from django.contrib import admin
from .models import customer


# Register your models here.
class display_customer(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone']


admin.site.register(customer,display_customer)
