from django.shortcuts import render
from rest_framework import permissions, viewsets

from models import Account
# from permissions import AccountPermissions
from serializers import AccountSerializer

# Create your views here.
# def bucketlists(request):
#     return render(request, 'bucketlists/bucketlists.html', {})


class AccountViewSet(viewsets.ModelViewSet):
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
