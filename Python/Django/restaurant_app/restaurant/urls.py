from django.urls import path
from . import views
from .views import FoodListView

urlpatterns = [
    path('', views.home, name='restaurant-home'),
    path('about/', views.about, name='restaurant-about'),
    path('shop/', views.shop, name='restaurant-shop'),
    # path('shop/', FoodListView.as_view(), name='restaurant-shop'),
    path('cart/', views.cart, name='cart'),
    path('reservation/', views.reservation, name='restaurant-reservation')
]