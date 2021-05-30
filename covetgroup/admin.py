from django.contrib import admin
from .models import SubscribedUser
# Register your models here.
class SubscribedUserAdmin(admin.ModelAdmin):
    list_display = ('email','created_at')

admin.site.register(SubscribedUser, SubscribedUserAdmin)