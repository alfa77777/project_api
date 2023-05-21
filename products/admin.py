from django.contrib import admin

from products.models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product", "comment_text"]
