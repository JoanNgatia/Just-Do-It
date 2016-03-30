from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import api

urlpatterns = [
    url(r'^users/$', api.AccountsList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', api.AccountsDetail.as_view()),
    url(r'^bucketlists/$', api.BucketListView.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', api.BucketlistDetail.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/$',
        api.BucketlistItemView.as_view()),
    url(r'^bucketlists/(?P<list_id>[0-9]+)/items/(?P<pk>[0-9]+)/$',
        api.BucketlistItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
