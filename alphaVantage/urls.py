"""
URL configuration for alphaVantage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import stockVisualizer.views
from stockVisualizer.views import MyLoginView, MyLogoutView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", stockVisualizer.views.home),
#     path('get_stock_data/', stockVisualizer.views.get_stock_data),
#     path('login/', MyLoginView.as_view(), name='login'),
#     path('logout/', MyLogoutView.as_view(), name='logout'),
# ]
# from django.urls import path
# from .views import home, get_stock_data, MyLoginView, MyLogoutView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', stockVisualizer.views.home, name='home'),
#     path('get_stock_data/', stockVisualizer.views.get_stock_data, name='get_stock_data'),
#     path('login/', MyLoginView.as_view(), name='login'),
#     path('logout/', MyLogoutView.as_view(), name='logout'),
# ]

# alphaVantage/alphaVantage/urls.py

from django.urls import path
import stockVisualizer.views as stock_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='login_page.html'), name='login'),
    path('stock_visualizer/', stock_views.home, name='home'),
    path('registration/', stock_views.save_user_info, name='registration'),
    path('get_stock_data/', stock_views.get_stock_data, name='get_stock_data'),
    path('logout/', stock_views.MyLogoutView.as_view(), name='logout'),
    path('test/', stock_views.test, name='test')
]
