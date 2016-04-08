from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.template import RequestContext

from bucketlist.models import Bucketlistitem
from bucketlist.forms.forms_bucketlist import BucketlistItemForm


class LoginRequiredMixin(object):
    """Enforce login for particular views."""

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class AllBucketlistitemsView(LoginRequiredMixin, TemplateView):
    """View to handle retrieval and creation of bucketlist items."""

    template_name = 'bucketlists/bucketitems.html'
    form_class = BucketlistItemForm

    def get_context_data(self, **kwargs):
        """Return dictionary representing passed in context."""
        context = super(
            AllBucketlistitemsView, self).get_context_data(**kwargs)
        context['bucketitems'] = Bucketlistitem.objects.filter(
            bucketlist_id=kwargs['pk'])
        # context['username'] = self.request.user.username
        context['bucketlistform'] = BucketlistItemForm()
        return context

    # def post(self, request, **kwargs):
    #     """Method to create a new bucketlist."""
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         new_bucketitem = form.save(commit=False)
    #         new_bucketitem.creator = self.request.user
    #         new_bucketitem.save()
    #         messages.success(
    #             request, 'New Bucketlist added successfully!')
    #         return redirect(
    #             '/bucketlists',
    #             context_instance=RequestContext(request)
    #         )
    #     else:
    #         messages.error(
    #             request, 'Error at creation!')
    #         return redirect(
    #             '/bucketlist',
    #             context_instance=RequestContext(request)
    #         )
