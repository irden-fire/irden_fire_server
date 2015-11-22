from django.contrib import admin
from authentication.models import UserData

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'user')

admin.site.register(UserData, UserDataAdmin)
