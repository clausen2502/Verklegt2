from django.http import HttpResponse
from django.shortcuts import render, redirect
def index(request):
    return HttpResponse(f"Response from {request.path}")



def finalize_contact_view(request, offer_id):
    if request.method == 'POST':
        # Hér getur þú vistað í session ef þú vilt
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
    if request.method == 'POST':
        payment_method = request.POST['payment_method']
        # Hér gætirðu farið áfram í næsta skref, s.s. kortaupplýsingar o.s.frv.
        return redirect('confirmation-page')  # eða næsta skref
    return render(request, 'finalization/payment.html', {'offer_id': offer_id})
