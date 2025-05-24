from django.contrib import admin

# Register your models here.

from products.models import category, product


admin.site.register(category)
admin.site.register(product)