from django.urls import path
from django.contrib import admin

from property import views

urlpatterns = [
    path(r'$', views.show_flats),
    path(r'search/$', views.show_flats),
    path(r'admin/', admin.site.urls),
]
