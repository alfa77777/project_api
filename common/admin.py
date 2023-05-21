from django.contrib import admin

from .models import Category, Brand


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "parent"]


@admin.register(Brand)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "logo"]

