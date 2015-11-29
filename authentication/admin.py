from django.contrib import admin
from authentication.models import UserData

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('pk', 'reg_date', 'client_name', 'contact_number', 'email')

admin.site.register(UserData, UserDataAdmin)
