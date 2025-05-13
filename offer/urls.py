from django.urls import path
from . import views

urlpatterns = [
    path('', views.offer_list, name='offer-list'),
    path('submit/<int:property_id>/', views.submit_offer, name='submit-offer'),
    path('my-offers/', views.offer_list, name='my-offers'),
    path('offers/<int:offer_id>/resubmit/', views.resubmit_offer, name='resubmit-offer'),
    path('offers/<int:offer_id>/delete/', views.delete_offer, name='delete-offer'),
    path('received/', views.received_offers, name='received_offers'),
    path('offer/<int:offer_id>/update/<str:new_status>/', views.update_offer_status, name='update-offer-status'),
]
