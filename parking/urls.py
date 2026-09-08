# url routes for this part of the project.
from django.urls import path
from . import views

app_name = "parking"

urlpatterns = [
    path("", views.home, name="home"),
    path("health/", views.health_check, name="health"),
    path("parking/", views.parking_list, name="list"),
    path("map/", views.map_view, name="map"),
    path("parking/add/", views.parking_create, name="create"),
    path("parking/<int:pk>/", views.parking_detail, name="detail"),
    path("parking/<int:pk>/edit/", views.parking_edit, name="edit"),
    path("parking/<int:pk>/delete/", views.parking_delete, name="delete"),
    path(
        "parking/<int:pk>/favourite/",
        views.toggle_favourite,
        name="toggle_favourite",
    ),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
]