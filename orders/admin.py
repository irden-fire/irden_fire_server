from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'contact_number', 'created')

admin.site.register(Order, OrderAdmin)
