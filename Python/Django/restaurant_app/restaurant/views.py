from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import food, reservation_detail, booking_detail, table, FoodType
from users.models import UserCart, UserOrder

# Create your views here.


class FoodListView(ListView):
    model = food
    template_name = 'restaurant/shop.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'foods'
    paginate_by = 5


def home(request):
    return render(request, template_name='restaurant/home.html')


def about(request):
    context = {
        'title' : 'About'
    }
    return render(request, template_name='restaurant/about.html', context=context)


def shop(request):
    if request.method=='GET' and request.GET.get('search'):
        context = {
            'title' : 'Shop',
            'foods' : food.objects.filter(name__contains=request.GET.get('search'))
        }
    else:
        context = {
            'title' : 'Shop',
            'foods' : food.objects.all
        }
    if request.method=='POST':
        if request.user.is_authenticated:
            # print(request.POST.get('food_name'))
            # print(request.POST.get('food_price'))
            # print(type(request.POST.get('food_quantity')))
            # print(request.POST.get('food_id'))
            user_Carts = UserCart.objects.all()
            flag = 1
            for user_cart in user_Carts:
                if user_cart.user == request.user and user_cart.food_name == request.POST.get('food_name'):
                    user_cart.add(request.POST.get('food_name'), request.POST.get('food_price'), request.POST.get('food_quantity'), request.POST.get('image_url'))
                    user_cart.get_total_price()
                    user_cart.save()
                    flag = 0
            if flag:
                user_Cart = UserCart()
                user_Cart.user = request.user
                user_Cart.add(request.POST.get('food_name'), request.POST.get('food_price'), request.POST.get('food_quantity'), request.POST.get('image_url'))
                user_Cart.get_total_price()
                user_Cart.save()
            return redirect('restaurant-shop')
        else:
            return redirect('login')
    return render(request, template_name='restaurant/shop.html', context=context)


@login_required
def cart(request):
    context = {
        'title' : 'Cart',
        'items' : [usercart  for usercart in UserCart.objects.all() if request.user==usercart.user],
        'payment' : False
    }
    if len(context['items']):
        context['payment'] = True
    
    if request.method=='POST' and len(context['items']) and request.POST.get('place_order'):
        userorder = UserOrder()
        userorder.user = request.user
        userorder.items = ""
        userorder.total = 0.0
        while len(context['items']):
            userorder.items += f"Item: {context['items'][0].food_name}   Quantity: {context['items'][0].quantity}  Price: {context['items'][0].food_price}\n"
            userorder.total += float(context['items'][0].food_price) * float(context['items'][0].quantity)
            UserCart.objects.get(user=request.user, food_name=context['items'][0].food_name).delete()
            context['items'].pop(0)
        userorder.save()
        return redirect('restaurant-home')
    
    if request.method=='POST':
        if request.user.is_authenticated:
            # print(UserCart.objects.all())
            # print(request.POST.get('food_name'))
            # print(UserCart.objects.all().exclude(user=request.user, food_name=request.POST.get('food_name')))
            UserCart.objects.get(user=request.user, food_name=request.POST.get('food_name')).delete()
            return redirect('restaurant-home')
        else:
            return redirect('login')
    return render(request, template_name='restaurant/cart.html', context=context)


def reservation(request):
    context = { 
        'title' : 'Reservation',
        "tables" : table.objects.all,
        "timings" : ["", "08:00AM-09:00AM", "09:00AM-10:00AM", "10:00AM-11:00AM", "11:00AM-12:00PM", "12:00PM-01:00PM"]
    }
    if request.method=='POST':
        # print(request.user.profile.phone)
        if request.user.is_authenticated and request.POST.get('table') and request.POST.get('timing'):
            reserve = reservation_detail()
            reserve.name = request.user.username
            reserve.phone = request.user.profile.phone
            reserve.table = request.POST.get('table')
            reserve.timing = request.POST.get('timing')
            reserve.save()
            return redirect('restaurant-home')
        elif request.POST.get('name') and request.POST.get('phone'):
            reserve = booking_detail()
            reserve.name = request.POST.get('name')
            reserve.phone = request.POST.get('phone')
            reserve.save()
            return redirect('restaurant-home')
        else:
            return render(request, template_name='restaurant/reservation_table.html', context=context)
    else:
        return render(request, template_name='restaurant/reservation_table.html', context=context)


