from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from bucketlist.views import authentication_view

urlpatterns = [
    # url(r'^$', views.index, name='dashboard'),
    url(r'^$', authentication_view.IndexView.as_view(), name='index'),
    url(r'^register$', authentication_view.RegistrationView.as_view(),
        name='register'),
    # url(r'^bucketlists/', views.all_bucketlists_view, name="all_bucketlists"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
