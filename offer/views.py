from django.http import HttpResponse

def index(request):
    return HttpResponse(f"Response from {request.path}")
