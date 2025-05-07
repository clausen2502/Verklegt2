from django.urls import path
from . import views

urlpatterns = [
    path('<int:offer_id>/', views.finalize_contact_view, name='finalize-offer'),
    path('<int:offer_id>/payment/', views.finalize_payment_view, name='finalize-payment'),
]