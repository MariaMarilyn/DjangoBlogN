from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_noticia, name='crear_noticia'),
    path('ver/<int:noticia_id>/', views.ver_noticia, name='ver_noticia'),
    path('editar/<int:noticia_id>/', views.editar_noticia, name='editar_noticia'),
    path('eliminar/<int:noticia_id>/', views.eliminar_noticia, name='eliminar_noticia'),
    path('', views.lista_noticias, name='lista_noticias'),
]