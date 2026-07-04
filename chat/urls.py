from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('hello/', views.hello, name='hello'),
    path('register/', views.register_view, name='register'),
    path('create-room/', views.create_room, name='create_room'),
    path('chat/<str:room_name>/', views.room, name='room'),

]
