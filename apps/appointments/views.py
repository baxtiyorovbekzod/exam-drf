from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Appointment
from .serializers import AppointmentSerializer
from ..users.permissions import IsPatientOrReadOnly


class AppointmentsViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsPatientOrReadOnly]
    
    serializer_class = AppointmentSerializer
    
    
    def get_queryset(self):
        user = self.request.user
        queryset = Appointment.objects.all()
        
        match user.role:
            case 'admin':
                return queryset
            case 'patient':
                return queryset.filter(patient=user)
            case 'doctor':
                return queryset.filter(doctor=user)
            case _:
                return queryset.none()
        
    
    def perform_destroy(self, instance):
        timeslot = instance.timeslot
        timeslot.is_available = True
        timeslot.save(update_fields=["is_available"])
        instance.delete()
    
    
    def perform_update(self, serializer):
        old_instance = self.get_object()
        old_slot = old_instance.timeslot

        instance = serializer.save()
        new_slot = instance.timeslot

        # agar timeslot o‘zgargan bo‘lsa
        if old_slot != new_slot:
            old_slot.is_available = True
            old_slot.save(update_fields=["is_available"])

            new_slot.is_available = False
            new_slot.save(update_fields=["is_available"])

        # agar status cancelled bo‘lsa
        if instance.status == "cancelled":
            new_slot.is_available = True
        new_slot.save(update_fields=["is_available"])