from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'user/user.html')

def get_user_by_id(request, id):
    return HttpResponse(f"Response from user ID {id}")
