from django.contrib import admin
from . models import *
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display=("user","user_type","contact")
# class OrderAdmin(admin.ModelAdmin):
#     list_display=("order","quantity",)

admin.site.register(Design)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Order)