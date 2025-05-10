from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from offer.models import PurchaseOffer
from property.models import Property

def offer_list(request):
    if not request.user.is_authenticated:
        # Show a limited view or message to guest users
        return render(request, 'offer/offer_guest.html')

    offers = PurchaseOffer.objects.filter(buyer=request.user)

    return render(request, 'offer/offer_list.html', {
        'offers': offers
    })

@login_required
def submit_offer(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == "POST":
        offer_price = request.POST.get("offer_price")
        expiration_date = request.POST.get("expiration_date")
        message = request.POST.get("message", "")

        PurchaseOffer.objects.create(
            buyer=request.user,
            property=property,
            amount=offer_price,
            expiration_date=expiration_date,
            message=message
        )

        return redirect("offer-confirmation")

    return render(request, "offer/submit_offer.html", {"property": property})
