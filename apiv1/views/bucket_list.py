"""This file defines the api endpoints for the bucketlist and items info."""

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
    """Handle the URL to list all bucketlists and create one.

    URL : /api/v1/bucketlists
    Args:
        To create a bucketlist:
            name - name of the bucketlist.
    Returns:
        POST/GET -- Dictionary containing bucketlist details inclusive of
                name,items contained, dates created or updated and the creator
    """

    queryset = Bucketlist.objects.all()
    serializer_class = bucketlistserializer.BucketlistSerializer
    search_fields = ('name', )

    def perform_create(self, serializer):
        """Associate bucketlist to an account,save data passed in request."""
        serializer.save(creator=self.request.user)


class BucketlistDetail(DefaultsMixin, generics.RetrieveUpdateDestroyAPIView):
    """Allow for retrieval of one bucketlist, its edition and deletion.

    URL : /api/v1/bucketlists/<list_id>
    Args:
        pk = list_id
        To update a bucketlist:
            name -  new name of the bucketlist.
    Returns:
        PUT/GET -- Dictionary containing bucketlist details inclusive of
                name,items contained, dates created or updated and the creator
        DELETE -- 204 status code
    """

    queryset = Bucketlist.objects.all()
    serializer_class = bucketlistserializer.BucketlistSerializer


class BucketlistItemView(DefaultsMixin, generics.CreateAPIView):
    """Allow for bucketlist item creation.

    URL : /api/v1/bucketlists/<list_id>/items/
    Args:
        pk = list_id
        To create a bucketlist item:
            name - name of the item.
    Returns:
        POST -- Dictionary containing the items details inclusive of
                name, status(done/not done) and dates created or updated.
    """

    serializer_class = bucketlistserializer.BucketlistitemSerializer
    search_fields = ('name', )

    def get_queryset(self):
        """Return specific bucketlist as per URL request."""
        list_id = self.kwargs['pk']
        return Bucketlistitem.objects.filter(bucketlist=list_id)


class BucketlistItemDetail(DefaultsMixin,
                           generics.UpdateAPIView, generics.DestroyAPIView):
    """Allow for bucketlist item edition and deletion.

    URL : /api/v1/bucketlists/<list_id>/items/<items_id>/
    Args:
        list_id = bucketlist_id
        pk = item_id
        To update a bucketlist item:
            name - new name of the item.
    Returns:
        PUT-- Dictionary containing bucketlist item  details inclusive of
                name, status(done/not done) and dates created or updated.
        DELETE -- 204 status code
    """

    serializer_class = bucketlistserializer.BucketlistitemSerializer

    def get_queryset(self):
        """Return specific bucketlistitem as per url request."""
        list_id = self.kwargs['list_id']
        item_id = self.kwargs['pk']
        bucketlistitem = Bucketlistitem.objects.filter(
            id=item_id, bucketlist=list_id)
        return bucketlistitem
