from django.urls import path
from .views import list_view, update_page, delete_page

urlpatterns = [
    path("list/", list_view, name='dlist'),
    path("<int:id>/update/", update_page),
    path("<int:id>/delete/", delete_page),
]