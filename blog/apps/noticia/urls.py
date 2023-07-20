from django.urls import path
from . import views

app_name = 'noticia'  

urlpatterns = [
    path('editar/<int:pk>/', views.editar_noticia, name='editar_noticia'),
    path('eliminar/<int:pk>/', views.eliminar_noticia, name='eliminar_noticia'),
]
