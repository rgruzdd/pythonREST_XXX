from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_teacher


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'student')

# from rest_framework.permissions import BasePermission, SAFE_METHODS
# from rest_framework import permissions
#
#
# class IsOwnerProfileOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.user == request.user
#
#
# class IsThisUserOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.id == request.user.id
