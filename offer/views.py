from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def offer_list(request):
    if not request.user.is_authenticated:
        return render(request, 'offer/offer_guest.html')

    # your real offer logic goes here
    return render(request, 'offer/offer_list.html', {
        # context for logged-in users
    })
