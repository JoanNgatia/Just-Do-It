from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from models import Account, Bucketlist
from permissions import IsAccountOwner
from serializers import AccountSerializer, BucketlistSerializer

# Create your views here.
# def bucketlists(request):
#     return render(request, 'bucketlists/bucketlists.html', {})


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

        return(permissions.IsAuthenticated(), IsAccountOwner(), )

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


class BucketList(generics.ListCreateAPIView):
    """Handle /api/v1/bucketlists/ path."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Associate bucketlist to an account."""
        serializer.save(owner=self.request.account)


class BucketlistDetail(generics.RetrieveUpdateDestroyAPIView):
    """Handle /api/v1/bucketlists/<bucketlist_id> path."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
