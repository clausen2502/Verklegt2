from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin-dashboard'),  # ← for /manager/
    path('dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete-user'),
    path('manager/delete-property/<int:property_id>/', views.delete_property, name='manager-delete-property'),

]
