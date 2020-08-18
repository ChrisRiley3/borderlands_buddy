from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_weapons, name='weapons'),
    path('<weapon_id>', views.weapon_detail, name='weapon_detail'),
]
