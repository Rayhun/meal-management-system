from django.urls import path

# local imports
from user_profile.views.profile import ProfileUpdateView, ProfileView
from user_profile.views.user import LoginView
app_name = 'user_profile'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/view/', ProfileView.as_view(), name='profile_view'),
    path(
        'profile/<int:pk>/update/', ProfileUpdateView.as_view(),
        name='profile_update'
    ),
]
