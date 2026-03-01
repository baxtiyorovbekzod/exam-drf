from django.db import models
from ..doctors.models import TimeSlot
from ..users.models import User


class Appointment(models.Model):
    class StatusChoice(models.TextChoices):
        Pending = 'pending', 'Pending' 
        Confirmed = 'confirmed', 'Confirmed' 
        Cancelled = 'cancelled', 'Cancelled'
        
    doctor = models.ForeignKey(User, related_name='doctor_appointment', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, related_name='patient_appointment', on_delete=models.CASCADE)
    timeslot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)
    status = models.CharField(choices=StatusChoice, default=StatusChoice.Pending)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['patient', 'timeslot']