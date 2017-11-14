from django.conf.urls import url
from address_session import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^addresses/$', views.AddressList.as_view()),
    url(r'^addresses/(?P<pk>[0-9]+)/$', views.AddressDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)