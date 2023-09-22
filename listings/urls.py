from django.urls import path
from .views import (
  listing_list, 
  listing_retrive, 
  listing_create, 
  listing_update,
  listing_delete
)

urlpatterns = [
    path("", listing_list, name='home'),
    path("listing/create", listing_create, name='create'),
    path("listing/<pk>/update/", listing_update, name='update'),
    path("listing/<pk>/delete/", listing_delete, name='delete'),
    path("listing/<pk>/", listing_retrive, name='list'),
]