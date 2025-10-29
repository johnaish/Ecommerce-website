from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "created_at")   # show these fields in list
    search_fields = ("name", "description")                     # enable search
    list_filter = ("category", "created_at")                    # enable filters
    ordering = ("-created_at",)                                 # newest first


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)                                    # show category name
    search_fields = ("name",)                                   # allow searching categories
