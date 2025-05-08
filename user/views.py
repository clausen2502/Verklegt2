from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'user/user.html')

def get_user_by_id(request, id):
    return HttpResponse(f"Response from user ID {id}")

# /user/register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)  # <-- See why it failed

    else:
        return render(request, template_name='user/register.html', context={
            'form': UserCreationForm()
        })
@login_required
def profile(request):
    return render(request, 'user/profile.html')