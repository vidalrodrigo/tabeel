from django.urls import re_path, path

from .views import (
    AboutViewSet,
    EmployeeViewSet
)

from .views_web import (
    index
)

urlpatterns = [
    # API
    re_path(r'^about/?$', AboutViewSet.as_view({'get': 'about'}), name='about'),
    re_path(r'^employee/create/?$', EmployeeViewSet.as_view({'post': 'create'}), name='create'),

    # Páginas HTML
    path('home/', index, name='index'),
    
]
