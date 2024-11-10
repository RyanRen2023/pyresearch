from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('add/', views.add_vehicle, name='add_vehicle'),
    path('edit/<int:row_id>/', views.edit_vehicle, name='edit_vehicle'),
    path('delete/<int:row_id>/', views.delete_vehicle, name='delete_vehicle'),
    path('export/', views.export_vehicles_to_csv, name='export_vehicles_to_csv'),
    path('reload/', views.reload_vehicles_from_csv, name='reload_vehicles_from_csv'),
    path('view/<int:row_id>/', views.view_vehicle, name='view_vehicle'),  # 添加查看车辆的路由

]