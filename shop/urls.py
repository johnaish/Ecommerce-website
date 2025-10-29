from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("checkout/", views.mpesa_checkout, name="mpesa_checkout"),
    path("signup/", views.signup, name="signup"),
]
