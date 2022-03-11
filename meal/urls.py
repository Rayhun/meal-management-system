from django.urls import path

# local imports
from meal import views
app_name = 'meal'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('todo/list/', views.TodoListView.as_view(), name='todo'),
    path('todo/create/', views.TodoCreateView.as_view(), name='todo_create'),
    path(
        'todo/update/<int:pk>/', views.TodoUpdateView.as_view(),
        name='todo_update'
    ),
]
