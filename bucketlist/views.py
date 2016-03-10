from django.shortcuts import render


# Create your views here.
def bucketlists(request):
    return render(request, 'bucketlists/bucketlists.html', {})
