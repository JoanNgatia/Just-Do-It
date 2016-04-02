"""Handle main django template views."""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from models import Bucketlist, Account
from forms import RegistrationForm


def index(request):
    """Landing page."""
    return render(request, 'bucketlists/dashboard.html')


@login_required
def all_bucketlists_view(request):
    """Render all bucketlists on page."""
    bucketlists = Bucketlist.objects.all()
    return render(request, 'bucketlists/bucketlists.html',
                  {'bucketlists': bucketlists})


@login_required
def single_bucketlist_view(request, pk):
    """Render single bucketlist detail."""
    bucketlist = get_object_or_404(Bucketlist, pk=pk)
    return render(request, 'bucketlist/bucketlists.html',
                  {'bucketlist': bucketlist})
