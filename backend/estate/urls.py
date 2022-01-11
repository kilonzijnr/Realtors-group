from django.urls import path
from . import views
urlpatterns = [
    path("", views.add_roperty, name="add_property"),
]