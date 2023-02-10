from django.contrib import admin

from core.models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'last_login']
    list_display = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name']


admin.site.register(User, UserAdmin)
