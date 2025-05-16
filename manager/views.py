from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from property.models import Property
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

def is_manager(user: User) -> bool:
    """
    Check if the user has a 'manager' attribute.

    Args:
        user (User): The Django User object.

    Returns:
        bool: True if user has 'manager' attribute, False otherwise.
    """
    return hasattr(user, 'manager')

@login_required
@user_passes_test(is_manager)
def delete_user(request: HttpRequest, user_id: int) -> HttpResponseRedirect:
    """
    Deletes a user from the database if they exist.

    Args:
        request (HttpRequest): The HTTP request object.
        user_id (int): The ID of the user to delete.

    Returns:
        HttpResponseRedirect: Redirects back to the admin dashboard.
    """
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        messages.success(request, "User deleted successfully.")
    except User.DoesNotExist:
        messages.error(request, "User not found.")
    return redirect('admin-dashboard')


@login_required
@user_passes_test(is_manager)
def delete_property(request: HttpRequest, property_id: int) -> HttpResponseRedirect:
    """
    Deletes a property from the database if it exists.

    Args:
        request (HttpRequest): The HTTP request object.
        property_id (int): The ID of the property to delete.

    Returns:
        HttpResponseRedirect: Redirects back to the admin dashboard.
    """
    try:
        property = Property.objects.get(id=property_id)
        property.delete()
        messages.success(request, "Property deleted successfully.")
    except Property.DoesNotExist:
        messages.error(request, "Property not found.")
    return redirect('admin-dashboard')


@login_required
@user_passes_test(is_manager)
def admin_dashboard(request: HttpRequest) -> HttpResponse:
    """
    Renders the admin dashboard displaying all users and properties.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page for the manager dashboard.
    """
    users = User.objects.all()
    properties = Property.objects.all()
    return render(request, "manager/dashboard.html", {
        'users': users,
        'properties': properties
    })
