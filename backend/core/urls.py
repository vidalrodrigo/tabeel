from django.urls import re_path

from .views import (
    AboutViewSet
)

urlpatterns = [
    re_path(r'^about/?$', AboutViewSet.as_view({'get': 'about'}), name='about'),
]
