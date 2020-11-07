from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    # sort the products by SKU using the ordering attribute
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# register our new classes alongside their respective models.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

