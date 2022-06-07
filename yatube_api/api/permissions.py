from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Проверка на авторство контента."""

    def has_object_permission(self, request, view, obj):
        if (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        ):
            return True
        return False
