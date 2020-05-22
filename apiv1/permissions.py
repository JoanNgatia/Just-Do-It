from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Define account permissions."""

    def has_object_permission(self, request, view, obj):
        """Check user associated with request is same object as account.

        Read permissions allowed to any request.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user
