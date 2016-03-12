from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^users/$', views.AccountsList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.AccountsDetail.as_view()),
    url(r'^bucketlists/$', views.BucketListView.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', views.BucketlistDetail.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/$',
        views.BucketlistItemView.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/(?P<pk_item>[0-9]+)/$',
        views.BucketlistItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
