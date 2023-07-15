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
# pylint: disable=E0611
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
# pylint: disable=E0401
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi

from rest_framework import routers

from books.api import viewset as booksviewsets

#criando instância do roteador "DefaultRouter". Objeto que contém os métodos e atributos definidos
# na classe DefaultRouter e pode ser usado para registrar rotas e gerar automaticamente URLs para as suas views.
route = routers.DefaultRouter() 

# pylint: disable=E1101
route.register(r'books/', booksviewsets.BooksViewSet, basename="Books")

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(route.urls))
]

# concateno as duplas urlpatterns (a minha e a do swagger) com +=
urlpatterns += [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] 