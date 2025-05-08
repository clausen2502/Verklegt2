from django.http import HttpResponse
from django.shortcuts import render, redirect
def index(request):
    return HttpResponse(f"Response from {request.path}")



def finalize_contact_view(request, offer_id):
    if request.method == 'POST':
        request.session['contact_info'] = {
            'offer_id': offer_id,
            'street_name': request.POST['street_name'],
            'city': request.POST['city'],
            'postal_code': request.POST['postal_code'],
            'country': request.POST['country'],
            'kennitala': request.POST['kennitala']
        }
        return redirect('finalize-payment', offer_id=offer_id)
    return render(request, 'finalization/contact_info.html', {'offer_id': offer_id})


def finalize_payment_view(request, offer_id):
    if request.method == "POST":
        method = request.POST.get("payment_method")

        if method == "card":
            return redirect("credit-card-form", offer_id=offer_id)
        elif method == "bank":
            return redirect("bank-transfer-form", offer_id=offer_id)
        elif method == "mortgage":
            return redirect("mortgage-form", offer_id=offer_id)
        else:
            # fallback eða error message
            return redirect("payment")

    return render(request, "finalization/payment.html", {"offer_id": offer_id})
def credit_card_form(request, offer_id):
    return render(request, "finalization/credit_card.html", {"offer_id": offer_id})

def bank_transfer_form(request, offer_id):
    return render(request, "finalization/bank_transfer.html", {"offer_id": offer_id})

def mortgage_form(request, offer_id):
    return render(request, "finalization/mortage.html", {"offer_id": offer_id})
