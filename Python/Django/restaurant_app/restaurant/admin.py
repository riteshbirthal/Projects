from django.contrib import admin
from .models import food, reservation_detail, booking_detail, FoodItem, FoodType, table

# Register your models here.

admin.site.register((food, reservation_detail, booking_detail, FoodItem, FoodType, table))