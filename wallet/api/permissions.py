from rest_framework import permissions

class IsUser(permissions.BasePermission) :
    def has_object_permission(self, request, view, obj):
        
        return obj.user == request.user


class IsOnBoard(permissions.BasePermission) :
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.is_onboard  

    def has_object_permission(self, request, view, obj):
         
        if request.method in permissions.SAFE_METHODS and (request.user.is_authenticated and request.user.profile.is_onboard)  : # safe method is a tuple containing get ,Options ,Head etc.
          return True
       
        return obj.author == request.user  and  (request.user.is_authenticated and request.user.profile.is_onboard)  
        
            
