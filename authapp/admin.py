from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authapp.models import ShopUser

admin.site.register(ShopUser, UserAdmin)
