from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import TimeSlot
from .serializers import TimeSlotSerializer
from ..users.permissions import IsDoctor, IsDoctorOrReadOnly


class TimeSlotViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsDoctorOrReadOnly]

    serializer_class = TimeSlotSerializer    
    
    def get_queryset(self):
        queryset = TimeSlot.objects.all()
        # if 
        # return queryset.filter(doctor=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user)
        return super().perform_create(serializer)