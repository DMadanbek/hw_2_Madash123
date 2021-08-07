"""hw_1_nurtazim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

    Домашнее задание 2.
Вывести на страницу список товаров - 127.0.0.1:8000/products/
Вывести на страницу один товар -  127.0.0.1:8000/products/<int:id>/
EXTRA: Создать модель Tag и связать с Product через ManyToManyField. На странице одного товара вывести тэги данного товара

"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from product import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.main_page_vievs),
    path("logout/", views.logout),
    path("login/", views.login),
    path("Category/<int:Category_id>/",views.category_vievs),
    path("products/<int:Product_id>/", views.product_item_views),
    path("add_product/",views.add_product),
    path("register/",views.register),
    path("check/",views.check),
    path('javascript/', views.javascript),
    path('activate/<str:code>', views.activate),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

