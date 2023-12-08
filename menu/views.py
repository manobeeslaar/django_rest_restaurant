from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view  

from .models import Item
from .serializers import ItemSerializer

# def item_list(request):
#     items = Item.objects.all()
#     item_list = []
#     for item in items:
#         item_list.append({
#             'name': item.name,
#             'description': item.description,
#             'price': item.price,
#             'image': item.image.url,
#             'category': item.category
#         })
    
#     return JsonResponse({'menu_items': item_list})

@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

def item_list_serialized(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse({'menu_items': serializer.data})

@api_view(['GET'])
def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)