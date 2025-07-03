from django.urls import re_path, path

from .views import (
    AboutViewSet, EmployeeViewSet,
    UserViewSet
)


urlpatterns = [
    re_path(r'^about/?$', AboutViewSet.as_view({'get': 'about'}), name='about'),
    re_path(r'^employee/create/?$', EmployeeViewSet.as_view({'post': 'create'}), name='create'),
    re_path(r'^user/login/?$', UserViewSet.as_view({'post': 'login'}), name='login'),
    re_path(r'^user/register/?$', UserViewSet.as_view({'post': 'register'}), name='register'),
]
