from django.contrib.auth.decorators import login_required
from offer.models import PurchaseOffer
from offer.purchase_offer_form import PurchaseOfferForm
from property.models import Property
from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.http import require_POST

def offer_list(request: HttpRequest) -> HttpResponse:
    """
    Displays a list of offers for authenticated users,
    or a guest message for unauthenticated users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered offer list or guest message.
    """
    if not request.user.is_authenticated:
        # Show a limited view or message to guest users
        return render(request, 'offer/offer_guest.html')

    offers = PurchaseOffer.objects.filter(buyer=request.user)

    return render(request, 'offer/offer_list.html', {
        'offers': offers
    })

@login_required
def submit_offer(request: HttpRequest, property_id: int) -> HttpResponse:
    """
    Allows an authenticated user to submit a purchase offer for a property.

    Args:
        request (HttpRequest): The HTTP request object.
        property_id (int): The ID of the property for the offer.

    Returns:
        HttpResponse: Rendered offer submission page or redirect on success.
    """
    property_obj = get_object_or_404(Property, id=property_id)

    if request.method == "POST":
        form = PurchaseOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.buyer = request.user
            offer.property = property_obj
            offer.save()
            messages.success(request, 'Your offer has been submitted!')
            return redirect("my-offers")
    else:
        form = PurchaseOfferForm()

    return render(request, "offer/submit_offer.html", {
        "property": property_obj,
        "form": form
    })

def resubmit_offer(request: HttpRequest, offer_id: int) -> HttpResponse:
    """
    Allows the buyer to resubmit an updated purchase offer.

    Args:
        request (HttpRequest): The HTTP request object.
        offer_id (int): The ID of the offer to resubmit.

    Returns:
        HttpResponse: Rendered offer resubmission page or redirect on success.
    """
    offer = get_object_or_404(PurchaseOffer, id=offer_id, buyer=request.user)
    property_obj = offer.property

    if request.method == 'POST':
        form = PurchaseOfferForm(request.POST, instance=offer)
        if form.is_valid():
            updated_offer = form.save(commit=False)
            updated_offer.status = 'pending'
            updated_offer.save()
            messages.success(request, 'Your offer has been resubmitted!')
            return redirect('property-detail', id=property_obj.id)
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
def delete_offer(request: HttpRequest, offer_id: int) -> HttpResponseRedirect:
    """
    Deletes an offer made by the logged-in user.

    Args:
        request (HttpRequest): The HTTP request object.
        offer_id (int): The ID of the offer to delete.

    Returns:
        HttpResponseRedirect: Redirect to offer list after deletion.
    """
    offer = get_object_or_404(PurchaseOffer, id=offer_id, buyer=request.user)
    offer.delete()
    messages.success(request, "Offer deleted successfully.")
    return redirect('offer-list')

@login_required
def received_offers(request: HttpRequest) -> HttpResponse:
    """
    Displays offers received by the logged-in seller.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered offers received page.
    """
    """Display all offers received for properties owned by the logged-in seller."""
    offers = PurchaseOffer.objects.filter(property__seller=request.user)
    return render(request, 'offer/offers_received.html', {'offers': offers})

@login_required
def update_offer_status(request: HttpRequest, offer_id: int, new_status: str) -> HttpResponseRedirect:
    """
    Updates the status of a received offer.

    Args:
        request (HttpRequest): The HTTP request object.
        offer_id (int): The ID of the offer to update.
        new_status (str): The new status to assign to the offer.

    Returns:
        HttpResponseRedirect: Redirect to received offers page.
    """
    offer = get_object_or_404(PurchaseOffer, id=offer_id)

    if offer.property.seller != request.user:
        messages.error(request, "You are not authorized to manage this offer.")
        return redirect("received_offers")

    valid_statuses = ['accepted', 'rejected', 'contingent']
    if new_status not in valid_statuses:
        messages.error(request, "Invalid status.")
        return redirect("received_offers")

    offer.status = new_status

    if new_status == 'contingent':
        contingent_message = request.POST.get('contingent_message', '').strip()
        offer.contingent_message = contingent_message

    offer.save()

    messages.success(request, f"Offer has been marked as {new_status.capitalize()}.")
    return redirect("received_offers")

