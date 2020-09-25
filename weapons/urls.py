from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_weapons, name='weapons'),
    path('<int:weapon_id>/', views.weapon_detail, name='weapon_detail'),
    path('add/', views.add_weapon, name='add_weapon'),
    path('edit/<int:weapon_id>/', views.edit_weapon, name='edit_weapon'),
]
