from django.urls import path

# local imports
from meal import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
]
