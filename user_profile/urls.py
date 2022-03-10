from django.urls import path

# local imports
from user_profile.views.profile import ProfileCreateView, ProfileView
app_name = 'user_profile'

urlpatterns = [
    path('profile/view/', ProfileView.as_view(), name='profile_view'),
    path(
        'profile/create/', ProfileCreateView.as_view(), name='profile_create'
    ),
]
