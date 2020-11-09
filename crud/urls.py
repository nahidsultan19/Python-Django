from django.urls import path
from . import views

urlpatterns = [
    path('', views.CrudApp, name='app'),
    path('list/', views.crudItemList, name='list'),
    path('update/<str:pk>/', views.crudItemUpdate, name='update')

]
