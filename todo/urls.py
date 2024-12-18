from django.urls import path

from todo import views

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("edit/<int:todo_id>", views.edit, name="edit"),
    path("delete/<int:todo_id>", views.delete, name="delete"),
]
