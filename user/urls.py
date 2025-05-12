from django.contrib.auth.views import LoginView
from user import views as user_views, views
from django.urls import path

urlpatterns = [
    # http://localhost:8000 (root)
    path('seller/<int:id>/', views.get_seller_by_id, name='seller-profile'),
    path('register/', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_display, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path("become-seller/", user_views.become_seller, name="become-seller"),
    path('my-properties.html/', views.my_properties, name='my-properties.html'),
    path('offers-received/', views.offers_received, name='offers-received'),
]