from django.urls import path
from . import views

app_name = 'todoApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('update/<str:pk>/', views.updateTodo, name='update'),
    path('delete/<str:pk>/', views.deleteTodo, name='delete')
]
