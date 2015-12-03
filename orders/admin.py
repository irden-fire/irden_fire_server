from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'created', 'desired_date', 'price', 'user_data')

admin.site.register(Order, OrderAdmin)
