from django.contrib import admin

from .models import Category, Ticket


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "priority", "status", "category", "created_at")
    list_filter = ("priority", "status", "category")
    search_fields = ("title", "description")
    autocomplete_fields = ("category",)
    date_hierarchy = "created_at"
