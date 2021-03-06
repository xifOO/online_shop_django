from django.shortcuts import render, redirect
from boots.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from payment import payment


@login_required()
def cart_add(request, id):
    """Добавляет предмет в корзину"""
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required()
def cart_clear(request):
    """Очищает корзину"""
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart_detail")


@login_required()
def cart_detail(request):
    """Корзина"""
    """Ссылка на оплату qiwi"""
    pay_url = payment.pay(amount=100)
    return render(request, 'cart.html', {'pay_url': pay_url})


@login_required()
def item_clear(request, id):
    """Удаляет предмет из корзины"""
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart:cart_detail")






