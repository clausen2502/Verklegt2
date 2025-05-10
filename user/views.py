from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from property.models import Property
from user.forms import UserProfileForm, UserForm
from user.models import SellerUser
from django.contrib import messages


def homepage(request):
    return render(request, 'user/user.html')

def get_user_by_id(request, id):
    seller = SellerUser.objects.select_related('user').get(user__id=id)
    properties = Property.objects.prefetch_related('photos').filter(seller=seller.user)

    return render(request, 'user/seller_profile.html', {
        'seller': seller,
        'properties': properties
    })

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
def profile_display(request):
    profile = request.user.userprofile
    return render(request, 'user/profile_display.html', {'profile': profile, 'user': request.user})

@login_required
def profile_edit(request):
    user = request.user
    profile = user.userprofile

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile_edit')
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'user/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
    })