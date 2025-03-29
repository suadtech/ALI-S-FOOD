from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/new/', views.create_reservation, name='create_reservation'),
    path('reservations/<int:pk>/edit/', views.edit_reservation, name='edit_reservation'),
    path('reservations/<int:pk>/cancel/', views.cancel_reservation, name='cancel_reservation'),
    path('menu/', views.menu, name='menu'),
]