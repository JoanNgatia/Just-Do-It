"""This file defines the api endpoints for the accounts/user info."""

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from bucketlist.models import Account
from apiv1.serializers import accountserializer


class AccountsList(generics.ListCreateAPIView):
    """Use DRF viewset to define Account CRUD methods.

    Handle the URL to create and account and list all accounts.
    URL : /api/v1/users/
    Args:
        To create a user:
            required - username , password
            optional - tagline
    Returns:
        Dictionary containing users' details inclusive of
        username, tagline and bucketlists created.
    """

    queryset = Account.objects.all()
    serializer_class = accountserializer.AccountSerializer

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
    """Allow admin access to user details.

    Handle the URL to list a particular users details.
    URL : /api/v1/user/<user_id>
    Args:
        pk -- the user id lookup field from the URL
    Returns:
        Dictionary containing a user's details inclusive of
        username, tagline and bucketlists created.
    """

    queryset = Account.objects.all()
    serializer_class = accountserializer.AccountSerializer
