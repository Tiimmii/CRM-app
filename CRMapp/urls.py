from django.urls import path
from . import views

app_name='leads'

urlpatterns = [
    path('lead-list', views.Lead_list.as_view(), name='lead-list'),
    path('detail/<str:pk>', views.Lead_detail.as_view(), name='lead-detail'),
    path('create',views.Lead_create.as_view(), name='lead-create'),
    path('update/<str:pk>', views.Lead_update.as_view(), name='lead-update'),
    path('delete/<str:pk>', views.Lead_delete.as_view(), name='lead-delete'),
    path('agentupdate/<str:pk>', views.Agent_Lead_update.as_view(), name='lead-agentupdate'),
    path('agentassign/<str:pk>', views.Agent_assign.as_view(), name='agentassign'),
    path('lead_categories',views.Lead_categories.as_view(), name='category'),
    path('categorydetail/<str:pk>', views.Lead_category_Detail.as_view(), name='category-detail'),
    path('new_leads/', views.New_lead_category.as_view(), name='new-leadcategory'),
    path('categoryleadupdate/<str:pk>', views.Lead_category_update.as_view(), name='category-leadupdate'),

]