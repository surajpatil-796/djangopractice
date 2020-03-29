from django.urls import path
from .views import list_view, detail_view

urlpatterns = [
    path("list/", list_view, name='list'),
    path("<int:id>/", detail_view )
]