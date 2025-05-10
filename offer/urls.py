from django.urls import path
from offer import views

urlpatterns = [
    path('my-offers/', views.offer_list, name='my-offers'),
]
