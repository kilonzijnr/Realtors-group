from django.urls import path,include,re_path
from . import views
from .views import *
urlpatterns = [
    path("add", views.add_roperty, name="add_property"),
    path("", views.home, name="home"),
    path('props/<id>/',views.props,name = 'props'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('<slug:slug>/blog-comments', views.blog_comments, name="blog_comments"),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
    #path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    #path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]