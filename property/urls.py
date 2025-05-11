from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="property-index"),
    path('create_property', views.create_property, name="create-property"),
    path('<int:id>/', views.get_property_by_id, name='property-detail'),
    path('test/', views.test_page, name='test-page'),
]