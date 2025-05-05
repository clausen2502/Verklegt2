from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000 (root)
    path('', views.index, name='user-index'),
    path('<int:id>/', views.get_user_by_id, name='user-by-id'),
]