from django.urls import path
from .views import AppointmentsViewSet

appointments_list = AppointmentsViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

appointments_detail = AppointmentsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', appointments_list, name='appointments-list'),
    path('<int:pk>/', appointments_detail, name='appointments-detail'),
]