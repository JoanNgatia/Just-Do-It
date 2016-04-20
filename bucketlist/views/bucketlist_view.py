from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.template import RequestContext

from bucketlist.models import Bucketlist
from bucketlist.forms.forms_bucketlist import BucketListForm


class LoginRequiredMixin(object):
    """Enforce login for particular views."""

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        """Add login required functionality to all decorated class views."""
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class AllBucketlistsView(LoginRequiredMixin, TemplateView):
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
            new_bucket = form.save(commit=False)
            new_bucket.creator = self.request.user
            new_bucket.save()
            messages.success(
                request, 'New Bucketlist added successfully!')
            return redirect(
                '/bucketlists',
                context_instance=RequestContext(request)
            )
        else:
            messages.error(
                request, 'Error at creation!')
            return redirect(
                '/bucketlist',
                context_instance=RequestContext(request)
            )


class BucketlistDetailView(LoginRequiredMixin, TemplateView):
    """View to handle retrieval and edition of single bucketlists."""

    def post(self, request, **kwargs):
        """Retrieve new details from request body."""
        bucketlist = Bucketlist.objects.filter(
            id=kwargs['pk'], creator=self.request.user).first()
        bucketlist.name = request.POST.get('name')
        bucketlist.save()
        messages.success(
            request, 'Bucketlist updated successfully!')
        return redirect('/bucketlists/',
                        context_instance=RequestContext(request))


class BucketlistDeleteView(LoginRequiredMixin, TemplateView):
    """View to handle deletion of a bucketlist."""

    def get(self, request, **kwargs):
        """Retrieve bucketlist id from request body and delete it."""
        bucketlist = Bucketlist.objects.filter(
            id=kwargs['pk'], creator=self.request.user).first()
        bucketlist.delete()
        messages.success(
            request, 'Bucketlist has been deleted successfully!')
        return redirect('/bucketlists/',
                        context_instance=RequestContext(request))
