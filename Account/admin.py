from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Account.models import User, Contact


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    list_display = ["username", "email", "phone", "is_admin", "real_address"]
    list_filter = ["is_admin" , "joined_at"]
    fieldsets = [
        ("اطلاعات شخصی",
         {"fields": ["first_name", "last_name", "phone", "real_address","post_code", "email", "username", "password"]}),
        ("دسترسی", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "phone", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["post_code"]
    ordering = ["post_code"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

admin.site.register(Contact)
