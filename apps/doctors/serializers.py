from rest_framework import serializers
from .models import TimeSlot
from django.utils import timezone

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        exclude = ['doctor', 'is_available']
        
    def validate(self, attrs):
        
        date = attrs.get("date")
        start = attrs.get("start_time")
        end = attrs.get("end_time")

        if start >= end:
            raise serializers.ValidationError(
                {"start_time": "Start time must be before end time."}
            )

        # 2) o‘tmish sanaga slot ochilmasin
        if date < timezone.localdate():
            raise serializers.ValidationError(
                {"date": "Date must be today or in the future."}
            )

        return attrs