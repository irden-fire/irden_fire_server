from django.contrib import admin
from prices.models import Price

class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')

admin.site.register(Price, PriceAdmin)
