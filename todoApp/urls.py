from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('update/<str:pk>/', views.updateTodo, name='update'),
    path('delete/<str:pk>/', views.deleteTodo, name='delete')
]
