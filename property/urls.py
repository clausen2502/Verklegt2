from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="property-index"),
    path('create_property', views.create_property, name="create-property"),
    path('<int:id>/', views.get_property_by_id, name='property-detail'),
    path('test/', views.test_page, name='test-page'),
    path('my-properties/', views.my_properties, name='my_properties'),
    path('edit-property/<int:id>/', views.edit_property, name='edit-property'),
    path('delete-property/<int:id>/', views.delete_property, name='delete-property'),
]