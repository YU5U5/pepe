from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro, name='registro'),  # Ruta para el registro
    path('token/', views.get_csrf_token, name='get_token'),  # Ruta para obtener el token CSRF
]

#dsff