from django.views.decorators.http import require_POST
from offer.models import PurchaseOffer
from property.models import Property, PropertyPhoto
from property.property_create_form import PropertyCreateForm
from django.contrib import messages
from user.models import SellerUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    properties = Property.objects.prefetch_related('photos').all()
    most_viewed = Property.objects.order_by('-view_count')[:3]

    locations = request.GET.getlist("location")
    bathrooms = request.GET.get("bathrooms")
    bedrooms = request.GET.get("bedrooms")
    size_from = request.GET.get("size_from")
    size_to = request.GET.get("size_to")
    price_from = request.GET.get("price_from")
    price_to = request.GET.get("price_to")
    types = request.GET.getlist("type")
    query = request.GET.get("q")
    sort_by = request.GET.get("sort_by")

    if query:
        properties = properties.filter(Q(street_name__icontains=query))
    if bedrooms:
        properties = properties.filter(bedrooms__gte=bedrooms)
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

    # Sorting logic
    if sort_by == "price_asc":
        properties = properties.order_by("price")
    elif sort_by == "price_desc":
        properties = properties.order_by("-price")
    elif sort_by == "name_asc":
        properties = properties.order_by("street_name")
    elif sort_by == "name_desc":
        properties = properties.order_by("-street_name")

    return render(request, "property/properties.html", {
        'properties': properties,
        'property_count': properties.count(),
        'most_viewed': most_viewed,
        'bathroom_filter': bathrooms,
        'locations': locations,
        'search_query': query,
        'types': types,
        'bedrooms': bedrooms,
        'price_from': price_from,
        'price_to': price_to,
        'size_from': size_from,
        'size_to': size_to,
        'sort_by': sort_by,
    })

def get_property_by_id(request, id):
    property = Property.objects.prefetch_related('photos').get(id=id)

    # Aukum fjölda heimsókna um 1
    property.view_count += 1
    property.save(update_fields=['view_count'])

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

@login_required
def my_properties(request):
    """Display properties owned by the logged-in seller."""
    properties = Property.objects.filter(seller=request.user)
    return render(request, 'property/my_properties.html', {'properties': properties})

@login_required
def edit_property(request, id):
    """Allow the seller to edit their property."""
    property = Property.objects.filter(id=id, seller=request.user).first()

    if not property:
        messages.error(request, "Property not found or you don't have permission to edit it.")
        return redirect('property-index')

    if request.method == 'POST':
        form = PropertyCreateForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            property = form.save(commit=False)
            property.save()

            for image in request.FILES.getlist('images'):
                PropertyPhoto.objects.create(image=image, property=property)

            messages.success(request, "Property updated!")
            return redirect('property-detail', id=property.id)
    else:
        form = PropertyCreateForm(instance=property)

    return render(request, 'property/edit_property.html', {
        'form': form,
        'property': property
    })


@require_POST
@login_required
def delete_property(request, id):
    """Allow the seller to delete their property"""
    property = get_object_or_404(Property, id=id, seller=request.user)
    property.delete()
    messages.success(request, "Property deleted!")
    return redirect('my_properties')
