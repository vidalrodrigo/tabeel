from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status, viewsets

from .utils import (
    get_response_headers
)

class AboutViewSet(viewsets.ViewSet):
    def about(self, request):
        try:
            return Response(
                {'message': 'TABEEL System'},
                status.HTTP_200_OK,
                headers=get_response_headers()
            )
        except Exception as e:
            return Response(
                {'message': f'acesso com erro: {str(e)}'},
                status.HTTP_403_FORBIDDEN,
                headers=get_response_headers()
            )