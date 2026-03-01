from rest_framework.serializers import ModelSerializer
from .models import Appointment


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ["doctor", "patient", "status", "created_at"]
        
    
    def create(self, validated_data):
        request = self.context['request']
        timeslot = validated_data["timeslot"]
        validated_data["patient"] = request.user
        validated_data["doctor"] = timeslot.doctor
        timeslot.is_available = False
        timeslot.save(update_fields=["is_available"])
        
        return super().create(validated_data)
    
    

    