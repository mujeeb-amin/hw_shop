from django.contrib import admin

# Register your models here.

from products.models import Category, Product


class productAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["title", "price", "category", "updated_date", "is_published"]
    list_display_links = ["title", "price"]
    list_editable = ["is_published"]
    list_filter = ["category"]
    # list_per_page = 2


admin.site.register(Category)
admin.site.register(Product, productAdmin)
