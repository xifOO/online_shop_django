from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Product, Category


@admin.register(Product)
class BootsAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass



