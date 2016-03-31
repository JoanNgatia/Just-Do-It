from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Define account permissions."""

    def has_object_permission(self, request, view, account):
        """Check user associated with request is same object as account.

        Read permissions allowed to any request.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return account.creator == request.user
