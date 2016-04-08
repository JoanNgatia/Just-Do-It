from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bucketlist.views import authentication_view, bucketlist_view, \
    bucketlistitem_view

urlpatterns = [
    url(r'^$', authentication_view.IndexView.as_view(), name='index'),
    url(r'^register$', authentication_view.RegistrationView.as_view(),
        name="register"),
    url(r'^login$', authentication_view.LoginView.as_view(), name="login"),
    url(r'^bucketlists/$', bucketlist_view.AllBucketlistsView.as_view(),
        name="all_bucketlists"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/edit/$',
        bucketlist_view.BucketlistDetailView.as_view(),
        name="single_bucketlist_edit"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/delete/$',
        bucketlist_view.BucketlistDeleteView.as_view(),
        name="single_bucketlist_delete"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/$',
        bucketlistitem_view.AllBucketlistitemsView.as_view(),
        name="bucketlistitems_get"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
