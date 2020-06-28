from django.urls import path
from .views import list_view, detail_view, update_page, delete_page

urlpatterns = [
    path("list/", list_view, name='list'),
    path("<int:id>/", detail_view ),
    path("<int:id>/update/", update_page),
    path("<int:id>/delete/", delete_page),
]