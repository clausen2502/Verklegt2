from django.urls import path
from .views import finalize_offer_view

urlpatterns = [
    path('<int:offer_id>/', finalize_offer_view, name='finalize-offer'),
]
