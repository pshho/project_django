from django.contrib import admin

from shop.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category, CategoryAdmin)

# 상품 등록
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category', 'price',
                    'stock', 'available_display', 'available_order',
                    'created', 'updated']
    list_filter = ['id', 'name', 'slug', 'category', 'price',
                    'stock', 'available_display', 'available_order',
                    'created', 'updated']
    prepopulated_fields = {'slug': ('name', )}
    list_editable = ['price', 'stock', 'available_display', 'available_order']
