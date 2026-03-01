from django.db import models

from ..users.models import User

class TimeSlot(models.Model):
    doctor = models.ForeignKey(User, related_name='timeslots', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(blank=True, default=True)