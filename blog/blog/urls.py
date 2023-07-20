"""
URL configuration for blog project.

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
from django.urls import path, include
from .views import index
from apps.noticia.views import acerca_de, contacto, listar_noticias, crear_noticia

urlpatterns = [
    path('', index, name='index'),
    path('noticia/', include('apps.noticia.urls')),  
    path('acerca-de/', acerca_de, name='acerca_de'),
    path('contacto/', contacto, name='contacto'),
    path('noticias', listar_noticias, name='listar_noticias'),
    path('crear/', crear_noticia, name='crear_noticia'),
]



