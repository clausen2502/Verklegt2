from django.shortcuts import render, redirect
from offer.models import PurchaseOffer
from property.models import Property, PropertyPhoto
from property.property_create_form import PropertyCreateForm
from user.models import SellerUser


def index(request):
    properties = Property.objects.prefetch_related('photos').all()
    return render(request, "property/properties.html", {
        "properties": properties,
        'property_count': properties.count()
    })

def get_property_by_id(request, id):
    property = Property.objects.prefetch_related('photos').get(id=id)

    user_offer = None
    if request.user.is_authenticated:
        user_offer = (
            PurchaseOffer.objects
            .filter(property=property, buyer=request.user)
        )

    return render(request, "property/single_property.html", {
        "property": property,
        "user_offer": user_offer
    })


def create_property(request):
    if request.method == "POST":
        form = PropertyCreateForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.seller = SellerUser.objects.get(user=request.user)
            property.save()

            for image in request.FILES.getlist('images'):
                PropertyPhoto.objects.create(image=image, property=property)

            return redirect('property-by-id', id=property.id)
    else:
        form = PropertyCreateForm()

    return render(request, 'property/create_property.html', {'form': form})

