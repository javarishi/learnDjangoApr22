"""learnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from pages.views import detailed_home_page, contactus_page
from products.views import view_product_page, create_product_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', detailed_home_page , name='home'),
    path('contact/', contactus_page , name='home'),
    path('product/<prId>/', view_product_page , name=''),
    path('create/', create_product_form , name=''),
]
