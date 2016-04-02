from django import forms

from bucketlist.models import Bucketlist


class BucketListForm(forms.ModelForm):
    class Meta:
        model = Bucketlist
        fields = ['name']
