from django.urls import path

from .views import item_list, item_detail

urlpatterns = [
    path("", item_list, name="item-list"),
    path("api/", item_list, name="item-list-serialized"),
    path("<int:pk>/", item_detail, name="item-detail"),
]
