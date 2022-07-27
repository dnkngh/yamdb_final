from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.is_admin
        return

    def has_object_permission(self, request, view, obj):
        if not request.user.is_anonymous:
            return request.user.is_admin
        return


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.is_admin
        return False


class AdminModeratorAuthorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_anonymous:
            return False
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_anonymous:
            return False
        return (
            obj.author == request.user
            or request.user.is_admin
            or request.user.is_moderator
        )
