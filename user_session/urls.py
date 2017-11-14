from django.conf.urls import url
from user_session import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^event-owners/$', views.EventOwnerList.as_view()),
    url(r'^event-owners/(?P<pk>[0-9]+)/$', views.EventOwnerDetail.as_view()),
    url(r'^app-users/$', views.AppUserList.as_view()),
    url(r'^app-users/(?P<pk>[0-9]+)/$', views.AppUserDetail.as_view()),
    url(r'^paths/(?P<pk>[0-9]+)/$', views.PathDetail.as_view()),
    url(r'^paths/$', views.PathList.as_view()),
    url(r'^login/$', views.login)
]

urlpatterns = format_suffix_patterns(urlpatterns)