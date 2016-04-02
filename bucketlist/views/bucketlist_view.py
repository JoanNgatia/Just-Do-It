from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext

from bucketlist.models import Bucketlist
from bucketlist.forms.forms_bucketlist import BucketListForm


class AllBucketlistsView(TemplateView):
    """View to handle retrieval and creation of bucketlists."""

    template_name = 'bucketlists/buckets.html'
    form_class = BucketListForm

    def get_context_data(self, **kwargs):
        """Return dictionary representing passed in context."""
        context = super(AllBucketlistsView, self).get_context_data(**kwargs)
        context['buckets'] = Bucketlist.objects.filter(
            creator=self.request.user)
        context['username'] = self.request.user.username
        context['bucketlistform'] = BucketListForm()
        return context

    def post(self, request, **kwargs):
        """Method to create a new bucketlist."""
        form = self.form_class(request.POST)
        if form.is_valid():
            new_bucket = form.save()
            new_bucket.creator = self.request.user
            new_bucket.save()
            messages.success(
                request, 'New Bucketlist added successfully!')
            return redirect(
                '/bucketlist',
                context_instance=RequestContext(request)
            )
        else:
            messages.error(
                request, 'Error at creation!')
            return redirect(
                '/bucketlist',
                context_instance=RequestContext(request)
            )
