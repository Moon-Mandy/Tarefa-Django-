from django.urls import path
from Site_app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.registrarPessoa, name='registrarPessoa'),
]
