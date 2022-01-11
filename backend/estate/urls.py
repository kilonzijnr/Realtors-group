from django.urls import path
from . import views
urlpatterns = [
    path("add", views.add_roperty, name="add_property"),
    path("", views.home, name="home"),
]