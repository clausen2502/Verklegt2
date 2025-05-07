from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000 (root)
    path('', views.index, name='user-homepage'),
    path('<int:id>/', views.get_user_by_id, name='user-by-id'),
    path('register/', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]