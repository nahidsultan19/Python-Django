from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import crudItem
from .serializers import ItemSerializer


@api_view(['GET'])
def CrudApp(request):
    api = {
        'ItemList': '/list/',
        'ItemCreate': '/create/',
        'ItemUpdate': '/update/<str:pk>/',
        'ItemDelete': '/Delete/<str:pk>/'
    }
    return Response(api)


@api_view(['GET', 'POST'])
def crudItemList(request):
    if request.method == 'GET':
        items = crudItem.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['POST', 'DELETE'])
def crudItemUpdate(request, pk):
    if request.method == 'POST':
        items = crudItem.objects.get(id=pk)
        serializer = ItemSerializer(instance=items, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        items = crudItem.objects.get(id=pk)
        items.delete()
        return Response('Deleted!')
