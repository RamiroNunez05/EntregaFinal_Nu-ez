from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('avatar-update/', views.AvatarUpdateView.as_view(), name='avatar-update'),
    path('profile-update/', views.ProfileUpdateView.as_view(), name='profile-update'),
]