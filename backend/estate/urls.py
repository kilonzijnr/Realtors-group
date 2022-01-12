from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path("add", views.add_roperty, name="add_property"),
    path("", views.home, name="home"),
    path('props/<id>/',views.props,name = 'props'),

    path('<slug:slug>/blog-comments', views.blog_comments, name="blog_comments"),
]