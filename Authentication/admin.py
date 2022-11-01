# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.conf import settings

# Create your models here.

from .models import User

class CustomUserAdmin(BaseUserAdmin):

    model = User
    list_display = ('user_name', 'first_name','email', 'user_date',)
    list_filter = ('user_name', 'first_name','email','user_date',)
    fieldsets = (
        (None, {'fields': ('first_name', 'email', 'password', 'user_name')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','user_name', 'password1', 'password2', 'is_staff')}
        ),
    )
    search_fields = ('email','user_name',)
    ordering = ('email','user_name',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, CustomUserAdmin)