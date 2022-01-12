from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^cities/', include('cities.urls')),
    url('admin/', admin.site.urls),
]