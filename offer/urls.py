from django.urls import path
from . import views

urlpatterns = [
    path('my-offers/', views.my_offers_view, name='my_offers'),
]
