from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('top/', views.home, name='home'),
    path('ent/', views.entertainment, name='ent'),
    path('health/', views.health, name='health'),
    path('scn/', views.science, name='science'),
    path('sport/', views.sport, name='sport'),
]