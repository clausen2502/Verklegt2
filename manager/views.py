from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from property.models import Property

def is_manager(user):
    return hasattr(user, 'manager')

@login_required
@user_passes_test(is_manager)
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        messages.success(request, "User deleted successfully.")
    except User.DoesNotExist:
        messages.error(request, "User not found.")
    return redirect('admin-dashboard')


@login_required
@user_passes_test(is_manager)
def delete_property(request, property_id):
    try:
        property = Property.objects.get(id=property_id)
        property.delete()
        messages.success(request, "Property deleted successfully.")
    except Property.DoesNotExist:
        messages.error(request, "Property not found.")
    return redirect('admin-dashboard')


@login_required
@user_passes_test(is_manager)
def admin_dashboard(request):
    users = User.objects.all()
    properties = Property.objects.all()
    return render(request, "manager/dashboard.html", {
        'users': users,
        'properties': properties
    })
