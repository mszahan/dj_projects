from rest_framework import permissions



class IsOwnerOrReadOnly(permissions.BasePermission):
    """"
    Custom permission to only allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to any request,
        # so we'll alays allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #write permission are only allowed to the owner of the snippet
        return obj.owner == request.user