from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.template import RequestContext

from bucketlist.models import Bucketlistitem, Bucketlist
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
        bucketlist = kwargs['pk']
        context['bucketlist'] = Bucketlist.objects.get(id=bucketlist)
        context['bucketitems'] = Bucketlistitem.objects.filter(
            bucketlist_id=kwargs['pk'])
        context['bucketlistform'] = BucketlistItemForm()
        return context

    def post(self, request, **kwargs):
        """Method to create a new bucketlist."""
        form = self.form_class(request.POST)
        if form.is_valid():
            item_name = request.POST.get('name')
            new_bucketitem = Bucketlistitem(
                name=item_name, bucketlist=Bucketlist.objects.get(id=kwargs['pk']))
            new_bucketitem.save()
            messages.success(
                request, 'New Bucketlistitem added successfully!')
            return redirect(
                '/bucketlists/',
                context_instance=RequestContext(request)
            )
        else:
            messages.error(
                request, 'Error at creation!')
            return redirect(
                '/bucketlists/',
                context_instance=RequestContext(request)
            )


class BucketlistitemUpdate(LoginRequiredMixin, TemplateView):
    """View logic to handle bucketlistitem name edition and marking as done."""

    def post(self, request, **kwargs):
        """Retrieve new details from request body."""
        bucketlist = kwargs['bucketlist']
        bucketlistitem = Bucketlistitem.objects.filter(
            id=kwargs['pk'], bucketlist_id=bucketlist).first()
        bucketlistitem.name = request.POST.get('name')
        bucketlistitem.done = False if bucketlistitem.done else True
        bucketlistitem.save()

        return redirect('/bucketlists/',
                        context_instance=RequestContext(request))


class BucketlistitemDelete(LoginRequiredMixin, TemplateView):
    """View logic to handle bucketlistitem deletion."""

    def get(self, request, **kwargs):
        """Retrieve bucketlist id from request body and delete it."""
        bucketlist = kwargs['bucketlist']
        bucketlistitem = Bucketlistitem.objects.filter(
            id=kwargs['pk'], bucketlist_id=bucketlist).first()
        bucketlistitem.delete()

        return redirect('/bucketlists/',
                        context_instance=RequestContext(request))
