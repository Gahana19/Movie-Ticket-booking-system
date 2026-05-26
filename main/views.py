from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_page(request):
    return render(request, 'index.html')
def login_page(request):
    return render(request, 'auth/login.html')


def main_dashboard(request):
    return render(request, 'admin_dashboard.html')
def cashier_dashboard(request):
    return render(request, 'cashier.html')
def customer_dashboard(request): 
    return render(request, 'customer.html')
