from django.contrib import admin

# Register your models here.

from products.models import category, product

class productAdmin(admin.ModelAdmin):
    model = product
    list_display = ["title", "price", "catagory", "updated_date","is_published"]
    list_display_links = ["title", "price"]
    list_editable = ["is_published"]
    list_filter = ["catagory"]
    # list_per_page = 2


admin.site.register(category)
admin.site.register(product, productAdmin)
