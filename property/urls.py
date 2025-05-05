from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/property
    path('', views.index, name='property-index'),
]