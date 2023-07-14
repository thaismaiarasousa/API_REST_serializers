"""
URL configuration for library project.

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
from django.urls import path, include

from rest_framework import routers

from books.api import viewset as booksviewsets

#criando instância do roteador "DefaultRouter". Objeto que contém os métodos e atributos definidos
# na classe DefaultRouter e pode ser usado para registrar rotas e gerar automaticamente URLs para as suas views.
route = routers.DefaultRouter() 

# pylint: disable=E1101
route.register(r'books/', booksviewsets.BooksViewSet, basename="Books")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(route.urls))
]
