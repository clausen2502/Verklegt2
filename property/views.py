from django.shortcuts import render, redirect
from property.models import Property, PropertyPhoto
from property.property_create_form import PropertyCreateForm
from django.contrib.auth.decorators import login_required


def index(request):
    properties = Property.objects.all()
    return render(request, "property/properties.html", {
        "properties": properties,
    })

def get_property_by_id(request, id):
    property = Property.objects.get(id=id)

    return render(request, "property/property_detail.html", {
        "property": property
    })


def create_property(request):
    if request.method == "POST":
        form = PropertyCreateForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.seller = request.user  # Set seller from logged-in user
            property.status = 'available'  # Force status to default value
            property.save()

            property_image = form.cleaned_data.get('image')  # assuming image field name is 'image'
            if property_image:
                PropertyPhoto.objects.create(image=property_image, property=property)

            return redirect('property-by-id', id=property.id)
    else:
        form = PropertyCreateForm()

    return render(request, 'property/create_property.html', {'form': form})