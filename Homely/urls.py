from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^employee/', include('Employee.urls', namespace="employee")),
    url(r'^discussion/', include('Discussion.urls', namespace="discussion")),
    url(r'^profile/', include('Profile.urls', namespace="profile")),
    url(r'^logoutPage/$', views.logoutPage, name="logoutPage"),
    url(r'^logout/$', views.logoutView, name="logout"),
    url(r'^login/$', views.loginView, name="login"),
    url(r'^register/$', views.registerPage, name="register"),
    url(r'^home/$', views.home, name="home"),
    url(r'^$', views.index, name="index"),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
