from django.urls import path

# local imports
from meal import views
app_name = 'meal'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
]
