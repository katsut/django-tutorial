from django.urls import path

from django.contrib.auth import views as auth_views
from todo import views

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html", next_page="/todo/"
        ),
        name="login",
    ),
    path(
        "logout/", auth_views.LogoutView.as_view(next_page="/todo/login"), name="logout"
    ),
    path("signup/", views.signup, name="signup"),
    path("create/", views.create, name="create"),
    path("edit/<int:todo_id>", views.edit, name="edit"),
    path("edit/<int:todo_id>/update", views.update, name="update"),
    path("delete/<int:todo_id>", views.delete, name="delete"),
]
