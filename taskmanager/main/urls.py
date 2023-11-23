from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('cart/<int:my_id>/', views.cartItem, name='cartItem'),
    path('order', views.order, name='order'),
    path('cats/', views.categories),
]
