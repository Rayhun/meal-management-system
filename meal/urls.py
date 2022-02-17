from django.urls import path

# local imports
from meal import views
from meal.views.user import RegisterView, LoginView
from meal.views.profile import ProfileCreateView, ProfileView
app_name = 'meal'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    # Profile
    path('profile/view/', ProfileView.as_view(), name='profile_view'),
    path(
        'profile/create/', ProfileCreateView.as_view(), name='profile_create'
    ),
]
