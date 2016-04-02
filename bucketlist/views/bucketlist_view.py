from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext

from bucketlist.models import Bucketlist


class AllBucketlistsView(TemplateView):
    """View to handle retrieval and creation of bucketlists."""

    template_name = 'bucketlists/buckets.html'

    def get_context_data(self, **kwargs):
        """Return dictionary representing passed in context."""
        context = super(AllBucketlistsView, self).get_context_data(**kwargs)
        context['buckets'] = Bucketlist.objects.filter(
            creator=self.request.user)
        context['username'] = self.request.user.username
        return context
