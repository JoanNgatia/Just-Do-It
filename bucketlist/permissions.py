from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    """Define account permissions."""

    def has_object_permission(self, request, view, account):
        """Check user associated with request is same object as account."""
        if request.user:
            return account == request.user
        return False
