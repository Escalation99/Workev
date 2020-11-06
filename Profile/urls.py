from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^changePassword/$', views.changePassword, name="changePassword"),
    url(r'^updateProfile/$', views.updateProfile, name="updateProfile"),
    url(r'^$', views.index, name="index"),
]
