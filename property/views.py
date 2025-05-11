from django.shortcuts import render, redirect
from offer.models import PurchaseOffer
from property.models import Property, PropertyPhoto
from property.property_create_form import PropertyCreateForm
from django.contrib import messages
from user.models import SellerUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def index(request):
    """Display a filtered list of properties based on user-selected criteria."""

    properties = Property.objects.prefetch_related('photos').all()

    # Extract filter values
    query = request.GET.get("q")
    size_from = request.GET.get("size_from")
    size_to = request.GET.get("size_to")
    price_from = request.GET.get("price_from")
    price_to = request.GET.get("price_to")
    types = request.GET.get.list("type")
    locations = request.GET.getlist("location")
    bedrooms = request.GET.get("bedrooms")
    bathrooms = request.GET.get("bathrooms")

    # Apply filters
    if query:
        properties = properties.filter(
            Q(street_name__icontains=query) |
            Q(description__icontains=query)
        )

    if size_from:
        properties = properties.filter(square_meters__gte=size_from)
    if size_to:
        properties = properties.filter(square_meters__lte=size_to)

    if price_from:
        properties = properties.filter(price__gte=price_from)
    if price_to:
        properties = properties.filter(price__lte=price_to)

    if types:
        properties = properties.filter(type__in=types)

    if locations:
        properties = properties.filter(postal_code__in=locations)

    if bedrooms:
        properties = properties.filter(bedrooms__gte=bedrooms)

    if bathrooms:
        properties = properties.filter(bathrooms__gte=bathrooms)

    type_choices = ["apartment", "house", "studio", "other"]
    size_choices = ["0", "40", "60", "70", "80", "90", "100", "150", "200", "300", "500"]
    room_choices = ["1", "2", "3", "4", "5"]
    price_choices = [
        "1000000", "5000000", "10000000", "15000000", "20000000",
        "25000000", "30000000", "40000000", "50000000", "60000000",
        "75000000", "100000000", "150000000", "200000000",
    ]

    return render(request, "user/user.html", {
        "properties": properties,
        "property_count": properties.count(),
        "selected_types": types,
        "size_choices": size_choices,
        "room_choices": room_choices,
        "price_choices": price_choices,
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

def is_seller(user: User) -> bool:
    return SellerUser.objects.filter(user=user).exists()

@login_required
def create_property(request):
    if not is_seller(request.user):
        return render(request, "user/become_seller_gate.html")
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


