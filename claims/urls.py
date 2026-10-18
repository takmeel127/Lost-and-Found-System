from django.urls import path
from . import views

app_name = "claims"

urlpatterns = [
    path("<str:item_type>/<int:item_id>/claim/", views.claim_item, name="claim_item"),
    path("my_claims/", views.my_claims, name="my_claims"),
]
