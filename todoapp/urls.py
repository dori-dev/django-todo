"""todoapp urls
"""
from django.urls import path
from .views import (
    home_view,
    todo_list_view,
    create_todo,
    delete_todo,
    edit_todo,
    about_view
)

app_name = "todoapp"
urlpatterns = [
    path("", home_view, name="home_url"),
    path("about/", about_view, name="about"),
    path("list/", todo_list_view, name="todo_list"),
    path('create/', create_todo, name='create_todo'),
    path('<id_>/delete/', delete_todo, name='delete_todo'),
    path('<id_>/edit/', edit_todo, name="edit_todo"),
]
