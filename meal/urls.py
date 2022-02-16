from django.urls import path

# local imports
from meal import views
from meal.views.user import register_request

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('register/request/', register_request, name='register_request'),
]
