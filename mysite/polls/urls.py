from django.urls import path
from . import views

urlpatterns = [
    path('bibliotecas/', views.listar_bibliotecas, name='listar_bibliotecas'),
    path('bibliotecas/buscarN/<str:nombre>/', views.buscar_biblioteca_por_nombre, name='buscar_biblioteca_por_nombre'),
    path('bibliotecas/buscarC/<str:ciudad>/', views.buscar_bibliotecas_por_ciudad, name='buscar_bibliotecas_por_ciudad'),
    path('bibliotecas/<str:nombre>/libros/', views.listar_libros_de_biblioteca, name='listar_libros_de_biblioteca'),
    path('bibliotecas/<str:nombre>/libros/buscarT/<str:titulo>/', views.buscar_libro_por_titulo_en_biblioteca, name='buscar_libro_por_titulo_en_biblioteca'),
    path('bibliotecas/<str:nombre>/libros/buscarA/<str:autor>/', views.buscar_libro_por_autor_en_biblioteca, name='buscar_libro_por_autor_en_biblioteca'),
    path('bibliotecas/<str:nombre>/libros/buscarE/<str:editorial>/', views.buscar_libro_por_editorial_en_biblioteca, name='buscar_libro_por_editorial_en_biblioteca'),
    path('libros/buscar/<str:titulo>/', views.buscar_libro_por_titulo, name='buscar_libro_por_titulo'),
    path('libros/buscar/disponibilidad/<str:titulo>/', views.buscar_libro_por_titulo_y_disponibilidad, name='buscar_libro_por_titulo_y_disponibilidad'),
    path('bibliotecas/nueva/', views.nueva_biblioteca, name='nueva_biblioteca'),
    path('libros/nuevo/', views.nuevo_libro, name='nuevo_libro'),
    path('bibliotecas/editar/<str:nombre>/', views.editar_biblioteca, name='editar_biblioteca'),
    path('libros/editar/<str:titulo>/', views.editar_libro, name='editar_libro'),
    path('bibliotecas/eliminar/<str:nombre>/', views.eliminar_biblioteca, name='eliminar_biblioteca'),
    path('bibliotecas/<str:nombre>/libros/eliminar/<str:titulo>/', views.eliminar_libro, name='eliminar_libro'),
]
