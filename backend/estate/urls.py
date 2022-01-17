from django.urls import path,include
from .import views 

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path("add", views.add_roperty, name="add_property"),
    path("props/<id>/",views.props,name = "props"),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('adminp/', views.adminp , name='adminp'),

]