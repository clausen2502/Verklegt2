from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="property-index"),
    path('create_property', views.create_property, name="create-property"),
]