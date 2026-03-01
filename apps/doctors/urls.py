from django.urls import path
from .views import TimeSlotViewSet

timeslot_list = TimeSlotViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

timeslot_detail = TimeSlotViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('timeslots/', timeslot_list, name='timeslot-list'),
    path('timeslots/<int:pk>/', timeslot_detail, name='timeslot-detail'),
]