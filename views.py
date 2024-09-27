from django.shortcuts import render
def register(request):
    return render(request,'/mysite/edriver/register.html')
def login_view(request):
    return render(request,'/mysite/edriver/login.html')
def order_driver(request):
    return render(request,'/mysite/edriver/order_driver.html')
def order_success(request):
    return render(request,'/mysite/edriver/order_success.html')
def track_driver(request):
    return render(request,'/mysite/edriver/track_driver.html')
def index(request):
    return render(request,'/mysite/edriver/index.html')
# Create your views here.
