from django.urls import path
from . import views

app_name = "upgrades"

urlpatterns = [
    path("main", views.MainView.as_view(), name="main"),
    path("", views.HomeView.as_view(), name="tutorial"),
]