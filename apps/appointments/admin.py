from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "doctor",
        "patient",
        "timeslot",
        "status",
        "created_at",
    )
    list_filter = ("status", "doctor")
    search_fields = (
        "doctor__username",
        "patient__username",
    )
    ordering = ("-created_at",)