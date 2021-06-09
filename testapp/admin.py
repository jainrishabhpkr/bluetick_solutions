from .models import *
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Users)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password',  'username')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',
                                         )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_store_owner',
                                       'is_superuser', 'is_onboarded', 'user_permissions')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('id', 'email', 'username', 'first_name',
                    'last_name',  'is_superuser', 'is_staff', 'is_active'
                    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('username',)


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", 'address')


@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "user", 'feedback')
