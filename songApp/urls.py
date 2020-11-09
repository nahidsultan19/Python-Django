from django.urls import path
from . import views


urlpatterns = [
    path('', views.Song, name='index'),
    path('song_list/', views.List, name='song_list'),
    path('<str:pk>/', views.Song, name='song_update'),
    path('delete_song/<str:pk>/', views.Delete_song, name='delete_song')
]
