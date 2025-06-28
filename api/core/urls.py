from django.urls import re_path

from .views import (
    AboutViewSet,
    EmployeeViewSet
)

urlpatterns = [
    re_path(r'^about/?$', AboutViewSet.as_view({'get': 'about'}), name='about'),
    re_path(r'^employee/create/?$', EmployeeViewSet.as_view({'post': 'create'}), name='create'),
]
