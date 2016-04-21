from django import forms

from bucketlist.models import Bucketlist, Bucketlistitem


class BucketListForm(forms.ModelForm):
    """Form for creation of a bucketlist.

    Extends from bucketlistmodel.
    """

    class Meta:
        model = Bucketlist
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
        }


class BucketlistItemForm(forms.ModelForm):
    """Form for creation of a bucketlistitem.

    Extends from bucketlistitem model.
    """

    class Meta:
        model = Bucketlistitem
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
        }
