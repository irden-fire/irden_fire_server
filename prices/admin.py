from django.contrib import admin
from prices.models import Price
from prices.models import PriceDescription

class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created', 'description_l18n')

class PriceDescriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'language', 'price')

admin.site.register(Price, PriceAdmin)
admin.site.register(PriceDescription, PriceDescriptionAdmin)
