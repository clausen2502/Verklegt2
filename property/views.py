from django.shortcuts import render, redirect
from offer.models import PurchaseOffer
from property.models import Property, PropertyPhoto
from property.property_create_form import PropertyCreateForm
from django.contrib import messages
from user.models import SellerUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def test_page(request):
    return render(request, 'property/test.html')


def index(request):
    properties = Property.objects.prefetch_related('photos').all()

    locations = request.GET.getlist("location")
    bathrooms = request.GET.get("bathrooms")
    bedrooms = request.GET.get("bedrooms")
    size_from = request.GET.get("size_from")
    size_to = request.GET.get("size_to")
    price_from = request.GET.get("price_from")
    price_to = request.GET.get("price_to")
    types = request.GET.getlist("type")
    query = request.GET.get("q")

    if query:
        properties = properties.filter(Q(street_name__icontains=query))
    if bathrooms:
        properties = properties.filter(bathrooms__gte=bathrooms)
    if locations:
        properties = properties.filter(postal_code__in=locations)
    if types:
        properties = properties.filter(type__in=types)
    if size_from:
        properties = properties.filter(square_meters__gte=size_from)
    if size_to:
        properties = properties.filter(square_meters__lte=size_to)
    if price_from:
        properties = properties.filter(price__gte=price_from)
    if price_to:
        properties = properties.filter(price__lte=price_to)

    return render(request, "property/properties.html", {
        'properties': properties,
        'property_count': properties.count(),
        'bathroom_filter': bathrooms,
        'locations': locations,
        'search_query': query,
        'types': types,
        'bedrooms': bedrooms,
        'price_from': price_from,
        'price_to': price_to,
        'size_from': size_from,
        'size_to': size_to,
    })

def get_property_by_id(request, id):
    property = Property.objects.prefetch_related('photos').get(id=id)

    user_offer = None
    if request.user.is_authenticated:
        user_offer = (
            PurchaseOffer.objects
            .filter(property=property, buyer=request.user)
            .first()
        )

    return render(request, "property/single_property.html", {
        "property": property,
        "user_offer": user_offer
    })

def is_seller(user: User) -> bool:
    return SellerUser.objects.filter(user=user).exists()

def create_property(request):
    if not request.user.is_authenticated:
        return redirect('/offers/my-offers/')

    if not is_seller(request.user):
        return render(request, "user/become_seller.html")

    if request.method == "POST":
        form = PropertyCreateForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                seller = SellerUser.objects.get(user=request.user)
            except SellerUser.DoesNotExist:
                messages.error(request, "You must be registered as a seller to list a property.")
                return redirect("property/create_property")

            property = form.save(commit=False)
            property.seller = seller.user
            property.save()

            for image in request.FILES.getlist('images'):
                PropertyPhoto.objects.create(image=image, property=property)

            return redirect('property-detail', id=property.id)
    else:
        form = PropertyCreateForm()

    return render(request, 'property/create_property.html', {
        'form': form,
        'user_is_seller': is_seller(request.user)
    })