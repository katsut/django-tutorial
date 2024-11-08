from django.urls import path

from . import views

app_name = "event"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:event_id>/", views.edit, name="edit"),
    path("<int:event_id>/update/", views.update, name="update"),
]
