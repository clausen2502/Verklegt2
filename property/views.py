from django.shortcuts import render, redirect
from property.models import Property, PropertyPhoto
from property.property_create_form import PropertyCreateForm


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
            property = form.save()
            property_image = form.cleaned_data.get('property_image')
            image = PropertyPhoto(image=property_image, property=property)
            image.save()
            return redirect(f'property-by-id', id=property.id)
        else:
            # form is invalid – re-render with errors
            return render(request, 'property/create_property.html', {
                'form': form
            })
    else:
        return render(request, 'property/create_property.html', {
            'form': PropertyCreateForm()
        })
