from django.urls import path
from . import views

app_name='leads'

urlpatterns = [
    path('', views.lead_list, name='lead-list'),
    path('detail/<str:pk>', views.lead_detail, name='lead-detail'),
    path('create',views.lead_create, name='lead-create'),
]