from django.http import HttpResponse
from django.shortcuts import render
from .models import PurchaseOffer
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse(f"Response from {request.path}")

def my_offers_view(request):
    return render(request, 'offer/my_offers.html')