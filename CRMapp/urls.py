from django.urls import path
from . import views

app_name='leads'

urlpatterns = [
    path('', views.Lead_list.as_view(), name='lead-list'),
    path('detail/<str:pk>', views.Lead_detail.as_view(), name='lead-detail'),
    path('create',views.Lead_create.as_view(), name='lead-create'),
    path('update/<str:pk>', views.Lead_update.as_view(), name='lead-update'),
    path('delete/<str:pk>', views.Lead_delete.as_view, name='lead-delete'),
    path('agentupdate/<str:pk>', views.Agent_Lead_update.as_view(), name='lead-agentupdate'),
]