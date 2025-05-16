from django.contrib.auth.decorators import login_required
from property.models import Property
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout
from user.models import SellerUser
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from user.forms import UserEditForm, UserProfileForm, CustomUserCreationForm


def is_seller(user: User) -> bool:
    """
    Checks if the user is registered as a seller.

    Args:
        user (User): The Django User object.

    Returns:
        bool: True if user is a seller, False otherwise.
    """
    return SellerUser.objects.filter(user=user).exists()

def is_manager(user: User) -> bool:
    """
    Checks if the user has a manager role.

    Args:
        user (User): The Django User object.

    Returns:
        bool: True if user has 'manager' attribute, False otherwise.
    """
    return hasattr(user, 'manager')

def homepage(request: HttpRequest) -> HttpResponse:
    """
    Renders the user homepage.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered homepage.
    """
    return render(request, 'user/user.html')


def get_user_by_id(request: HttpRequest, id: int) -> HttpResponse:
    """
    Displays a seller's profile and their properties.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The user ID.

    Returns:
        HttpResponse: Rendered seller profile page.
    """
    seller = SellerUser.objects.select_related('user').get(user__id=id)
    properties = Property.objects.prefetch_related('photos').filter(seller=seller.user)

    return render(request, 'user/seller_profile.html', {
        'seller': seller,
        'properties': properties
    })


def register(request: HttpRequest) -> HttpResponse:
    """
    Handles user registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered registration page or redirect on success.
    """
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
def profile_display(request: HttpRequest) -> HttpResponse:
    """
    Displays the logged-in user's profile.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered profile display page.
    """
    profile = request.user.userprofile
    return render(request, 'user/profile_display.html', {
        'profile': profile,
        'user': request.user,
    })


@login_required
def profile_edit(request: HttpRequest) -> HttpResponse:
    """
    Allows the user to edit their profile information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered profile edit page or redirect on success.
    """
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


def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    """
    Logs out the current user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the homepage.
    """
    logout(request)
    return redirect('user-homepage')


@login_required
def become_seller(request: HttpRequest) -> HttpResponse:
    """
    Allows a user to register as a seller.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered become seller page or redirect on success.
    """
    if is_manager(request.user):
        messages.error(request, "Admins cannot become sellers.")
        return redirect("profile")

    if is_seller(request.user):
        messages.info(request, "You are already registered as a seller.")
        return redirect("profile")

    if request.method == "POST":
        seller_type = request.POST.get("seller_type")
        logo = request.FILES.get("logo")
        cover_image = request.FILES.get("cover_image")
        bio = request.POST.get("bio")
        street = request.POST.get("street")
        city = request.POST.get("city")
        postal_code = request.POST.get("postal_code")

        SellerUser.objects.create(
            user=request.user,
            seller_type=seller_type,
            logo=logo,
            cover_image=cover_image,
            bio=bio,
            street=street,
            city=city,
            postal_code=postal_code
        )

        messages.success(request, "You are now registered as a seller!")
        return redirect("create-property")

    return render(request, "user/become_seller.html")



def get_seller_by_id(request: HttpRequest, id: int) -> HttpResponse:
    """
    Displays a seller's profile by their ID.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The seller ID.

    Returns:
        HttpResponse: Rendered seller profile page or redirect if not found.
    """
    try:
        seller = SellerUser.objects.select_related('user').get(id=id)
    except SellerUser.DoesNotExist:
        return redirect('user-homepage')

    properties = Property.objects.prefetch_related('photos').filter(seller=seller.user)

    return render(request, 'user/seller_profile.html', {
        'seller': seller,
        'properties': properties
    })


def about_view(request: HttpRequest) -> HttpResponse:
    """
    Displays the 'About Us' page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered about us page.
    """
    return render(request, 'user/about_us.html')

def calculator_view(request: HttpRequest) -> HttpResponse:
    """
    Displays the mortgage calculator page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered calculator page.
    """
    return render(request, 'user/calculator.html')



