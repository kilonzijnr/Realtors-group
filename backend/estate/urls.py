from django.urls import path
from . import views


urlpatterns=[
  
    path('rate/<project_id>/',views.rate,name ='rate'),
    
]