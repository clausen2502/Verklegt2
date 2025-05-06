from django.shortcuts import render
from property.models import Property
from property.property_create_form import PropertyCreateForm


def index(request):
    properties = Property.objects.all()
    return render(request, "property/properties.html", {
        "properties": properties,
    })

def get_property_by_id(request, id):
    property = Property.objects.get(id=id)

    return render(request, "property/properties.html", {
        "property": property
    })

def create_property(request):
    if request.method == "POST":
        print(1)
    else:
        return render(request, 'property/create_property.html', {
            'form': PropertyCreateForm()
        })