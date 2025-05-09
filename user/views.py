from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from property.models import Property
from user.models import SellerUser


def homepage(request):
    return render(request, 'user/user.html')

def get_user_by_id(request, id):
    seller = SellerUser.objects.select_related('user').get(user__id=id)
    properties = Property.objects.prefetch_related('photos').filter(seller=seller.user)

    return render(request, 'user/seller_profile.html', {
        'seller': seller,
        'properties': properties
    })

# /user/register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)

    else:
        return render(request, template_name='user/register.html', context={
            'form': UserCreationForm()
        })
@login_required
def profile(request):
    return render(request, 'user/profile.html')