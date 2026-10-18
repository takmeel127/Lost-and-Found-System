# items/urls.py
from django.urls import path
from . import views

app_name = "items"

urlpatterns = [
    # Upload pages
    path("lost/upload/", views.lost_item_upload, name="lost_item_upload"),
    path("found/upload/", views.found_item_upload, name="found_item_upload"),

    # List pages
   path("lost&found/list/", views.lost_and_found_list, name="lost_and_found_list"),
   

    # Detail pages
    path("<str:item_type>/<int:item_id>/detail/", views.item_detail, name="item_detail"),
]
