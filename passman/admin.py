from django.contrib import admin
from .models import Category, Site, Password

from django_otp.admin import OTPAdminSite

admin.site.__class__ = OTPAdminSite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'url', 'created_at', 'updated_at')
    search_fields = ('name', 'url', 'category__name')


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ('id', 'site', 'username', 'url', 'created_at', 'updated_at')
    search_fields = ('username', 'url', 'site__name')
