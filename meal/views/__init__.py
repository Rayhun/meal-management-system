from .dashboard import DashboardView
from .todo import (
    TodoListView, TodoCreateView, TodoUpdateView, TodoDetailView
)
from .market import (
    MarketCreateView, MarketListView, MarketUpdateView
)
from .deposet import DeposetCerateView, DeposetListView, DeposetUpdateView


__all__ = [
    'DashboardView', 'TodoListView', 'TodoCreateView', 'TodoUpdateView',
    'TodoDetailView', 'MarketCreateView', 'MarketListView',
    'MarketUpdateView', 'DeposetCerateView', 'DeposetListView',
    'DeposetUpdateView'
]
