from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status, viewsets
from .serializers import (
    EmployeeSerializer
)
from .service import (
    EmployeeService
)

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

class EmployeeViewSet(viewsets.ViewSet):
    service = EmployeeService()

    def create(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            employee = self.service.create_employee(serializer.validated_data)
            response_serializer = EmployeeSerializer(employee)
            data = {
                "message": "Funcionário criado com sucesso.",
                "result": response_serializer.data
            }
            return Response(
                data=data,
                status=status.HTTP_201_CREATED,
                headers=get_response_headers()
            )
        except Exception as e:
            return Response(
                data={"message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                headers=get_response_headers()
            )
