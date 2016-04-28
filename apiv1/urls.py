"""This file defines the urls to access the api endpoints."""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import accounts, bucket_list

urlpatterns = [
    url(r'^users/$', accounts.AccountsList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', accounts.AccountsDetail.as_view()),
    url(r'^bucketlists/$', bucket_list.BucketListView.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        bucket_list.BucketlistDetail.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/$',
        bucket_list.BucketlistItemView.as_view()),
    url(r'^bucketlists/(?P<list_id>[0-9]+)/items/(?P<pk>[0-9]+)/$',
        bucket_list.BucketlistItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
