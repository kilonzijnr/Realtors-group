from django.urls import path
from .import views


urlpatterns=[
  
    path('rate/<property_id>/',views.rate,name ='rate'),
    
]