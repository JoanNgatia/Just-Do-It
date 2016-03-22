from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions, status, authentication, \
    filters
from rest_framework.response import Response
from models import Account, Bucketlist, Bucketlistitem
from serializers import AccountSerializer, BucketlistSerializer, \
    BucketlistitemSerializer
from rest_framework.renderers import TemplateHTMLRenderer, \
    JSONRenderer


class DefaultsMixin(object):
    """Default reusable settings for authentication,
    permissions and filtering.
    """

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
    )


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

        return(permissions.IsAuthenticated(), )

    def create(self, request):
        """Override viewsets .save method to allow for password hashing."""
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
    """Allow admin access to user details."""

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class BucketListView(DefaultsMixin, generics.ListCreateAPIView):
    """Handle /api/v1/bucketlists/ path.

    Allow for retrieval of all bucketlists and bucketlist creation.
    """

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    search_fields = ('name', )
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'bucketlists/bucketlists.html'

    def perform_create(self, serializer):
        """Associate bucketlist to an account,save data passed in request."""
        serializer.save(creator=self.request.user)


class BucketlistDetail(DefaultsMixin, generics.RetrieveUpdateDestroyAPIView):
    """Handle /api/v1/bucketlists/<bucketlist_id> path.

    Allow for retrieval of one bucketlist, its edition and deletion.
    """

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class BucketlistItemView(DefaultsMixin, generics.CreateAPIView):
    """Handle /api/v1/bucketlists/<bucketlist_id>/items path.

    Allow for bucketlist item creation.
    """

    serializer_class = BucketlistitemSerializer
    search_fields = ('name', )

    def get_queryset(self):
        """Return specific bucketlist as per URL request."""
        list_id = self.kwargs['pk']
        return Bucketlistitem.objects.filter(bucketlist=list_id)


class BucketlistItemDetail(DefaultsMixin,
                           generics.RetrieveUpdateDestroyAPIView):
    """Handle /api/v1/bucketlists/<bucketlist_id>/items/<item_id>/path.

    Allow for edition and deletion of a bucketlistitem.
    """

    serializer_class = BucketlistitemSerializer

    def get_queryset(self):
        """Return specific bucketlistitem as per url request."""
        list_id = self.kwargs['list_id']
        bucketlistitem = Bucketlistitem.objects.filter(bucketlist=list_id)
        return bucketlistitem
