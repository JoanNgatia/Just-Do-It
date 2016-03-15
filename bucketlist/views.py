from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from models import Account, Bucketlist, Bucketlistitem
from permissions import IsOwnerOrReadOnly
from serializers import AccountSerializer, BucketlistSerializer, \
    BucketlistitemSerializer


class AccountsList(generics.ListAPIView):
    """Use DRF viewset to define Account CRUD methods."""

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        """Set access permissions to Account model."""
        # allow only account owner to update or delete an account.
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(), )

        # allow any user to create an account.
        if self.request.method == 'POST':
            return (permissions.AllowAny(), )

        return(permissions.IsAuthenticated(), IsOwnerOrReadOnly(), )

    def create(self, request):
        """Override viesets .save method to allow for passwor hashing."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data,
                            status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad Request',
            'message': 'Account could not be created with given details.'
        }, status=status.HTTP_400_BAD_REQUEST)


class AccountsDetail(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class BucketListView(generics.ListCreateAPIView):
    """Handle /api/v1/bucketlists/ path.

    Allow for retrieval of all bucektlists and bucketlist creation.
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Associate bucketlist to an account,save data passed in request."""
        serializer.save(creator=self.request.user)


class BucketlistDetail(generics.RetrieveUpdateDestroyAPIView):
    """Handle /api/v1/bucketlists/<bucketlist_id> path.

    Allow for retrieval of one bucketlist, its edition and deletion.
    """

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class BucketlistItemView(generics.ListCreateAPIView):
    """Handle /api/v1/bucketlists/<bucketlist_id>/items path.

    Allow for bucketlist item creation.
    """

    serializer_class = BucketlistitemSerializer

    def get_queryset(self):
        """Return specific bucketlist as per URL request."""
        list_id = self.kwargs['pk']
        return Bucketlistitem.objects.filter(bucketlist=list_id)


class BucketlistItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """Handle /api/v1/bucketlists/<bucketlist_id>/items/<item_id>/path.

    Allow for edition and deletion of a bucketlistitem.
    """

    serializer_class = BucketlistitemSerializer

    def get_queryset(self):
        """Return specific bucketlistitem as per url request."""
        list_id = self.kwargs['list_id']
        bucketlistitem = Bucketlistitem.objects.filter(bucketlist=list_id)
        return bucketlistitem
