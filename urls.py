from django.contrib import admin
from django.urls import path,include
from . import views
#from edriver.urls import urls as edriver_urls



urlpatterns = [
    path('', include ('edriver_urls')), 
    # other paths

    #path('admin/', admin.site.urls, name='admin'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('order_driver/', views.order_driver, name='order_driver'),
    path('order_success/', views.order_success, name='order_success'),
    path('track_driver/', views.track_driver, name='track_driver'),
]
#raymond
