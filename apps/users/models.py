from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    class RoleChoice(models.TextChoices):
        ADMIN = 'admin', 'Admin' 
        DOCTOR = 'doctor', 'Doctor'  
        PATIENT = 'patient', 'Patient'
    
    role = models.CharField(blank=True, choices=RoleChoice, default=RoleChoice.PATIENT, max_length=7)


class DoctorProfile(models.Model):
    
    class GenderChoice(models.TextChoices):
        MALE = 'male', 'Erkak'
        FEMALE = 'female', 'Ayol'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=127)
    experience_years = models.PositiveIntegerField()
    gender = models.CharField(blank=True, choices=GenderChoice, default=GenderChoice.MALE, max_length=7)
    
    
class PatientProfile(models.Model):
    class GenderChoice(models.TextChoices):
        MALE = 'male', 'Erkak'
        FEMALE = 'female', 'Ayol'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(blank=True, choices=GenderChoice, default=GenderChoice.MALE, max_length=7)