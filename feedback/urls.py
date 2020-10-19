from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback, name='feedback'),
    path('add/', views.add_feedback, name='add_feedback'),
]
