from django.urls import path
from . import views


urlpatterns = [
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart_detail', views.cart_detail, name='cart_detail'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
]