from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactInfoForm
from offer.models import PurchaseOffer
from .forms import CreditCardForm
from .forms import BankTransferForm


def index(request):
    return HttpResponse(f"Response from {request.path}")



def finalize_contact_view(request, offer_id):
    countries = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina",
        "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
        "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana",
        "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
        "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo",
        "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica",
        "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
        "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
        "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
        "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica",
        "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
        "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
        "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",
        "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
        "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria",
        "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea",
        "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda",
        "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",
        "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
        "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan",
        "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan",
        "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
        "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
        "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
        "Yemen", "Zambia", "Zimbabwe"
    ]

    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            request.session['contact_info'] = form.cleaned_data
            request.session['contact_info']['offer_id'] = offer_id
            return redirect('finalize-payment', offer_id=offer_id)
    else:
        form = ContactInfoForm()

    return render(request, 'finalization/contact_info.html', {
        'form': form,
        'offer_id': offer_id,
        'countries': countries,
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

    return render(request, "finalization/payment.html", {
        "offer_id": offer_id,
        'current_step': 'payment'
    })

def credit_card_form(request, offer_id):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['method'] = 'card'
            request.session['payment_data'] = data
            return redirect('review-page', offer_id=offer_id)
    else:
        form = CreditCardForm()
    return render(request, 'finalization/credit_card.html', {
        'form': form,
        'offer_id': offer_id,
        'current_step': 'payment'
    })

def bank_transfer_form(request, offer_id):
    if request.method == 'POST':
        form = BankTransferForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.copy()
            data['amount'] = str(data['amount'])              # Decimal fix
            data['transfer_date'] = str(data['transfer_date'])  # Date fix
            request.session['bank_data'] = data
            return redirect('review-page', offer_id=offer_id)
    else:
        form = BankTransferForm()

    return render(request, 'finalization/bank_transfer.html', {
        'form': form,
        'offer_id': offer_id,
        'current_step': 'bank'
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

    offer = get_object_or_404(PurchaseOffer, id=offer_id)

    # Ensure only the buyer of the offer can finalize it
    if offer.buyer != request.user:
        messages.error(request, "You are not authorized to finalize this offer.")
        return redirect("my-offers")

    # Ensure the offer is accepted OR contingent
    if offer.status not in ['accepted', 'contingent']:
        messages.error(request, "Only accepted or contingent offers can be finalized.")
        return redirect("my-offers")

    if offer.property.status != 'sold':
        offer.property.status = 'sold'
        offer.property.save()

    offer.status = 'finalized'
    offer.save()


    return render(request, 'finalization/confirmation.html', {
        'offer_id': offer_id,
        'contact_info': contact_info,
        'payment_info': payment_info,
        'current_step': 'confirmation'
    })





