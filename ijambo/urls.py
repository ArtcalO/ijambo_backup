from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.connexion, name='login'),
    path('logout/', views.deconexion, name='logout'),
]
