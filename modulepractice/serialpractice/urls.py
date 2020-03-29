from django.urls import path
from serialpractice.views import api_detail_view, api_delete_view, api_update_view, api_create_view
app_name='serialpractice'

urlpatterns=[ 
    path("<int:id>/" , api_detail_view ),
    path("<int:id>/aupdate" , api_update_view),
    path("<int:id>/adelete" , api_delete_view),
     path("create" , api_create_view)
]