from rest_framework import generics, permissions, authentication, \
    filters
from bucketlist.models import Bucketlist, Bucketlistitem
from apiv1.serializers import bucketlistserializer


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


class BucketListView(DefaultsMixin, generics.ListCreateAPIView):
    """Handle /api/v1/bucketlists/ path.

    Allow for retrieval of all bucketlists and bucketlist creation.
    """

    queryset = Bucketlist.objects.all()
    serializer_class = bucketlistserializer.BucketlistSerializer
    search_fields = ('name', )

    def perform_create(self, serializer):
        """Associate bucketlist to an account,save data passed in request."""
        serializer.save(creator=self.request.user)


class BucketlistDetail(DefaultsMixin, generics.RetrieveUpdateDestroyAPIView):
    """Handle /api/v1/bucketlists/<bucketlist_id> path.

    Allow for retrieval of one bucketlist, its edition and deletion.
    """

    queryset = Bucketlist.objects.all()
    serializer_class = bucketlistserializer.BucketlistSerializer


class BucketlistItemView(DefaultsMixin, generics.CreateAPIView):
    """Handle /api/v1/bucketlists/<bucketlist_id>/items path.

    Allow for bucketlist item creation.
    """

    serializer_class = bucketlistserializer.BucketlistitemSerializer
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

    serializer_class = bucketlistserializer.BucketlistitemSerializer

    def get_queryset(self):
        """Return specific bucketlistitem as per url request."""
        list_id = self.kwargs['list_id']
        bucketlistitem = Bucketlistitem.objects.filter(bucketlist=list_id)
        return bucketlistitem
