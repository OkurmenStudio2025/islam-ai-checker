from django.contrib import admin
from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "telegram_id")
    search_fields = ("name", "telegram_id")
    ordering = ("name",)
    list_filter = ("name",)

    fieldsets = (
        (None, {
            "fields": ("name", "telegram_id"),
        }),
    )
