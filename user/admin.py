from django.contrib import admin
from property.models import Property

class PropertyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or hasattr(request.user, 'manager')

admin.site.register(Property, PropertyAdmin)
from django.contrib import admin

# Register your models here.
