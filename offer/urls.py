from django.urls import path
from . import views

urlpatterns = [
    path('', views.offer_list, name='offer-list'),  # offers/
    path('submit/<int:property_id>/', views.submit_offer, name='submit-offer'),  # offers/submit/4/
    path('my-offers/', views.offer_list, name='my-offers'),  # NEW: offers/my-offers/
]
