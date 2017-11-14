from django.conf.urls import url
from event_session import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^events/$', views.EventList.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)