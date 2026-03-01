from django.contrib import admin
from .models import TimeSlot


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor", "start_time", "end_time", "is_available")
    list_filter = ("is_available", "doctor")
    search_fields = ("doctor__username",)
    ordering = ("start_time",)