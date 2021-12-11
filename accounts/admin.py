from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
# Register your models here.

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('user_email', 'user_name',)
    list_filter = ('user_email', 'user_name', 'is_active', 'is_staff')
    ordering = ('user_email',)
    list_display = ('user_email', 'user_name',
                    'is_active', 'is_staff','is_superuser')
    fieldsets = (
        (None, {'fields': ('user_email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser',)}),
        ('Personal', {'fields': ('phone_nymber','address','avatar')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_email', 'user_name','phone_number','address','avatar', 'password1', 'password2', 'is_active', 'is_staff','is_superuser')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)