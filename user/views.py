from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from property.models import Property
from user.forms import UserProfileForm, CustomUserCreationForm, UserEditForm
from user.models import SellerUser
from django.contrib.auth.models import User

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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration was successful! You can now log in.")
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'user/register.html', {'form': form})

@login_required
def profile_display(request):
    profile = request.user.userprofile
    return render(request, 'user/profile_display.html', {'profile': profile, 'user': request.user})

@login_required
def profile_edit(request):
    user = request.user
    profile = user.userprofile

    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'user/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
    })

def logout_view(request):
    logout(request)
    return redirect('user-homepage')
