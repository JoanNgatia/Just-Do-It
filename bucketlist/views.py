"""Handle main django template views."""
from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect
from models import Bucketlist


def index(request):
    """Landing page."""
    return render(request, 'bucketlists/dashboard.html')


# @login_required
# def bucketlists(request, bucketid):
#     """Bucketlist Manipulation"""
#     data = {}
#     data['bucketid'] = bucketid
#     return render(request, 'bucketlists.html', data)


@login_required
def bucket_list(request):
    bucketlists = Bucketlist.objects.all()
    return render(request, 'bucketlists/bucketlists.html', {'bucketlists': bucketlists})
