from django.urls import path
from user import views
from django.contrib.auth.views import LoginView
from user import views as user_views

urlpatterns = [
    # http://localhost:8000 (root)
    path('seller/<int:id>/', views.get_seller_by_id, name='seller-profile'),
    path('register/', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_display, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path("become-seller/", user_views.become_seller, name="become-seller"),
    path('about/', views.about_view, name='about'),
    path('calculator/', views.calculator_view, name='calculator'),
    path('favourites/', views.favourites_list, name='favourites-list'),
    path('favourites/toggle/<int:property_id>/', views.toggle_favorite, name='toggle-favorite'),


]