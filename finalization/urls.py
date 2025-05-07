from django.urls import path
from . import views

urlpatterns = [
    path('<int:offer_id>/', views.finalize_offer_view, name='finalize-offer'),
]
