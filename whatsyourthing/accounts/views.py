from django.shortcuts import render
from django.http import HttpResponse
from django import template
from .models import *
from .forms import OrderForm

register = template.Library()

# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()
    last_five = orders.order_by('-date_created')[:5]
    context = {'total': total_orders,
               'delivered': delivered,
               'pending': pending,
               'last_five': last_five,
               'customers': customers,
               'orders': orders,
               }

    return render(request, 'accounts/dashboard.html', context)

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count':order_count}
    return render(request, 'accounts/customer.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        print(request.POST)
        
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)