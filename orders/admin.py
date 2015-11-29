from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'created','client_name', 'contact_number')

admin.site.register(Order, OrderAdmin)
