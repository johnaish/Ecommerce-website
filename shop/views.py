from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Product, Cart, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
    item.save()
    return redirect("cart_detail")

@login_required
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, "shop/cart_detail.html", {"cart": cart})

@login_required
def mpesa_checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    total = cart.total_amount() if cart else 0
    return render(request, "shop/checkout.html", {"cart": cart, "total": total})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("product_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
