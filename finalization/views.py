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
    return render(request, 'finalization/contact_info.html', {
        'offer_id': offer_id,
        'current_step': 'contact'
    })


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

    return render(request, "finalization/payment.html", {
        "offer_id": offer_id,
        'current_step': 'payment'
    })

def credit_card_form(request, offer_id):
    if request.method == 'POST':
        request.session['payment_data'] = {
            'method': 'card',
            'cardholder_name': request.POST.get('cardholder_name'),
            'card_number': request.POST.get('card_number'),
            'expiry': request.POST.get('expiry_date'),
            'cvc': request.POST.get('cvc'),
        }
        return redirect('review-page', offer_id=offer_id)
    return render(request, "finalization/credit_card.html", {
        "offer_id": offer_id,
        "current_step": "payment"
    })

def bank_transfer_form(request, offer_id):
    if request.method == 'POST':
        request.session['payment_data'] = {
            'method': 'bank',
            'recipient_name': request.POST.get('recipient_name'),
            'account_number': request.POST.get('account_number'),
            'kennitala': request.POST.get('kennitala'),
            'bank_number': request.POST.get('bank_number'),
            'payment_info': request.POST.get('payment_info'),
            'amount': request.POST.get('amount'),
            'currency': request.POST.get('currency'),
            'transfer_date': request.POST.get('transfer_date'),
        }
        return redirect('review-page', offer_id=offer_id)
    return render(request, "finalization/bank_transfer.html", {
        "offer_id": offer_id,
        "current_step": "payment"
    })

def mortgage_form(request, offer_id):
    if request.method == 'POST':
        request.session['payment_data'] = {
            'method': 'mortgage',
            'provider': request.POST.get('mortgage_provider')
        }
        return redirect('review-page', offer_id=offer_id)
    return render(request, "finalization/mortage.html", {
        "offer_id": offer_id,
        "current_step": "payment"
    })


def review_view(request, offer_id):
    contact_info = request.session.get('contact_info', {})
    payment_info = request.session.get('payment_data', {})

    return render(request, 'finalization/review.html', {
        'offer_id': offer_id,
        'contact_info': contact_info,
        'payment_info': payment_info,
        'current_step': 'review'
    })


def confirmation_view(request, offer_id):
    contact_info = request.session.get('contact_info', {})
    payment_info = request.session.get('payment_data', {})

    return render(request, 'finalization/confirmation.html', {
        'offer_id': offer_id,
        'contact_info': contact_info,
        'payment_info': payment_info,
        'current_step': 'confirmation'
    })
