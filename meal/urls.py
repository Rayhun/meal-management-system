from django.urls import path

# local imports
from meal import views
from meal.views.ajax import load_ajax, need_item_load_ajax
app_name = 'meal'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('todo/list/', views.TodoListView.as_view(), name='todo'),
    path('todo/create/', views.TodoCreateView.as_view(), name='todo_create'),
    path(
        'todo/update/<int:pk>/', views.TodoUpdateView.as_view(),
        name='todo_update'
    ),
    path(
        'todo/details/<int:pk>/', views.TodoDetailView.as_view(),
        name='todo_details'
    ),
    # ajax load
    path(
        'todo/load/', load_ajax, name='todo_load'
    ),
    path(
        'need/item/load/', need_item_load_ajax, name='need_item_load'
    ),
]
