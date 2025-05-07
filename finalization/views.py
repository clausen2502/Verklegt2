from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse(f"Response from {request.path}")

def finalize_offer_view(request, offer_id):
    return render(request, 'finalization/finalize_offer.html')
