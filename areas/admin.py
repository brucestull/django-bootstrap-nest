# areas\admin.py

from django.contrib import admin

from .models import Area


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_area")
    search_fields = ("name",)
