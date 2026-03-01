from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin' 
    

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'doctor' 


class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'patient' 


class IsDoctorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.doctor == request.user
        )
    
    
class IsPatientOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.patient == request.user
        )
    
    
class IsAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.admin == request.user
        )


