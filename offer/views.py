from django.contrib.auth.decorators import login_required
from offer.models import PurchaseOffer
from offer.purchase_offer_form import PurchaseOfferForm
from property.models import Property
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from django.views.decorators.http import require_POST


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
    property_obj = get_object_or_404(Property, id=property_id)

    if request.method == "POST":
        offer_price = request.POST.get("offer_price")
        expiration_date = request.POST.get("expiration_date")
        message = request.POST.get("message", "")

        PurchaseOffer.objects.create(
            buyer=request.user,
            property=property_obj,
            amount=offer_price,
            expiration_date=expiration_date,
            message=message
        )

        return redirect("offer-confirmation")

    return render(request, "offer/submit_offer.html", {"property": property_obj})

def resubmit_offer(request, offer_id):
    offer = get_object_or_404(PurchaseOffer, id=offer_id, buyer=request.user)
    property_obj = offer.property

    if request.method == 'POST':
        form = PurchaseOfferForm(request.POST, instance=offer)
        if form.is_valid():
            updated_offer = form.save(commit=False)
            updated_offer.status = 'pending'  # reset status
            updated_offer.save()
            messages.success(request, 'Your offer has been resubmitted!')
            return redirect('offer-list')
    else:
        form = PurchaseOfferForm(instance=offer)

    return render(request, 'offer/resubmit_offer.html', {
        'form': form,
        'property': property_obj,
        'offer': offer,
        'resubmitting': True
    })

@require_POST
@login_required
def delete_offer(request, offer_id):
    offer = get_object_or_404(PurchaseOffer, id=offer_id, buyer=request.user)
    offer.delete()
    messages.success(request, "Offer deleted successfully.")
    return redirect('offer-list')