from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from ..utils.admin import BaseAdminMixin


class UserAdmin(BaseAdminMixin, BaseUserAdmin):
    list_readonly_not_superuser_fields = (
        'is_superuser', 'is_staff',
        'last_login', 'date_joined'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
