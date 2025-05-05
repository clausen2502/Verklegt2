from django.shortcuts import render
from property.models import Property

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