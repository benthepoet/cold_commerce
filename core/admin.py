from django.contrib import admin

from .models import Category, Product, ProductVariant

class ProductVariantInline(admin.StackedInline):
    model = ProductVariant

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_category')

    def get_category(self, obj):
        return obj.category.name
    get_category.admin_order_field = 'category'
    get_category.short_description = 'Category'

    inlines = [
        ProductVariantInline,
    ]

admin.site.register(Category)
