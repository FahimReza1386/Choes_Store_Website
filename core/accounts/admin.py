from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "is_staff",
        "is_superuser",
        "is_verified",
    )
    list_filter = ("email", "is_superuser", "is_verified")
    searching_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (
            "Authentication",
            {
                "fields": (
                    "email",
                    "password",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
        (
            "Group Permissions",
            {
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "Importent Dates",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
