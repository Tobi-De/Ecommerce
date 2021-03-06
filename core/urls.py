from django.urls import path

from .views import home, checkout, product

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("checkout/", checkout, name="checkout"),
    path("product/", product, name="product"),
]
