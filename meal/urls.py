from django.urls import path

# local imports
from meal import views
from meal.views.user import RegisterView, LoginView

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
