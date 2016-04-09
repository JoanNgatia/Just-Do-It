"""This file defines the urls to access the api endpoints."""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import accountsview, bucketlistview

urlpatterns = [
    url(r'^users/$', accountsview.AccountsList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', accountsview.AccountsDetail.as_view()),
    url(r'^bucketlists/$', bucketlistview.BucketListView.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        bucketlistview.BucketlistDetail.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/$',
        bucketlistview.BucketlistItemView.as_view()),
    url(r'^bucketlists/(?P<list_id>[0-9]+)/items/(?P<pk>[0-9]+)/$',
        bucketlistview.BucketlistItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
