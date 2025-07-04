"""
URL configuration for hw_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from products.views import (
    get_products,
    get_product,
    create_product,
    update_product,
    delete_product,
)

app_name = "products"

urlpatterns = [
    path("", get_products, name="product_list"),  # /products/
    path("<int:product_id>/", get_product, name="product_get"),  # /products/4
    path("create/", create_product, name="product_create"),  # /products/
    path(
        "update/<int:product_id>/", update_product, name="product_update"
    ),  # /products/
    path(
        "delete/<int:product_id>/", delete_product, name="product_delete"
    ),  # /products/
]
