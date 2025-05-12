from django.urls import path
from . import views

urlpatterns = [
    path('<int:offer_id>/', views.finalize_contact_view, name='finalize-offer'),
    path('<int:offer_id>/payment/', views.finalize_payment_view, name='finalize-payment'),
    path("finalize/<int:offer_id>/payment/card/", views.credit_card_form, name="credit-card-form"),
    path("finalize/<int:offer_id>/payment/bank/", views.bank_transfer_form, name="bank-transfer-form"),
    path("finalize/<int:offer_id>/payment/mortgage/", views.mortgage_form, name="mortgage-form"),
    path('finalize/<int:offer_id>/review/', views.review_view, name='review-page'),

]

