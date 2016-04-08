from django import forms

from bucketlist.models import Bucketlist, Bucketlistitem


class BucketListForm(forms.ModelForm):
    """Form for creation of a bucketlist.

    Extends from bucketlistmodel.
    """

    class Meta:
        model = Bucketlist
        fields = ['name']


class BucketlistItemForm(forms.ModelForm):
    """Form for creation of a bucketlistitem.

    Extends from bucketlistitem model.
    """

    class Meta:
        model = Bucketlistitem
        fields = ['name']
