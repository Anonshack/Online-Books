from django.urls import path
from .views import (
    UserListView,
    add_todo,

    todo_list,
    TodoListView,

    TodoUpdateView,
    TodoDeleteView,
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='users-list'),
    path('add-todo/', add_todo, name='add-todo'),

    path('todo-list/', todo_list, name='todo-list'),
    path('todo/<int:pk>/', TodoListView.as_view(), name='this-user'),

    path('todos/todo-update/<int:pk>/', TodoUpdateView.as_view(), name='todo-update'),
    path('todos/todo-delete/<int:pk>/', TodoDeleteView.as_view(), name='todo-delete'),
]
