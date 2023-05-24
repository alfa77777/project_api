from django.contrib import admin

from products.models import Product, Comment, LikeDislike


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "type"]


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product", "comment_text"]
