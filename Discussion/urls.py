from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^deleteReplies/(?P<delete_id>[0-9]+)$',
        views.deleteReplies, name="deleteReplies"),
    url(r'^editDiscussion/(?P<update_id>[0-9]+)$',
        views.editDiscussion, name="editDiscussion"),
    url(r'^deleteDiscussion/(?P<delete_id>[0-9]+)$',
        views.deleteDiscussion, name="deleteDiscussion"),
    url(r'^addDiscussion/$', views.addDiscussion, name="addDiscussion"),
    url(r'^detailUser/(?P<post_id>[0-9]+)/$',
        views.detailUser, name="detailUser",),
    url(r'^detail/(?P<post_id>[0-9]+)/$',
        views.detail, name="detail",),
    url(r'^indexUser/$', views.indexUser, name="indexUser"),
    url(r'^$', views.index, name="index"),
]
