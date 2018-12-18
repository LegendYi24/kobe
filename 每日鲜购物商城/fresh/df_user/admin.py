from django.contrib import admin
from .models import *
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["uname","upwd"]
admin.site.register(UserInfo,UserInfoAdmin)