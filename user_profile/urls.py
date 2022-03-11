from django.urls import path

# local imports
from user_profile.views.profile import ProfileUpdateView, ProfileView
from user_profile.views.user import LoginView, RegisterView, LogOutView
app_name = 'user_profile'

urlpatterns = [
    path('logout/', LogOutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/view/', ProfileView.as_view(), name='profile_view'),
    path(
        'profile/<int:pk>/update/', ProfileUpdateView.as_view(),
        name='profile_update'
    ),
]
