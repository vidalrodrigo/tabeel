from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    EmployeeSerializer,
    UserSerializer
)
from .service import (
    EmployeeService
)

from .utils import (
    get_response_headers
)

class AboutViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def about(self, request):
        try:
            return Response(
                {'message': 'TABEEL System'},
                status.HTTP_200_OK,
                headers=get_response_headers()
            )
        except Exception as e:
            print(str(e))
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
            print(str(e))
            return Response(
                data={"message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                headers=get_response_headers()
            )

class UserViewSet(viewsets.ViewSet):

    def login(self, request):
        try:
            user = get_object_or_404(User, email=request.data['email'])
            if not user.check_password(request.data['password']):
                return Response(
                    {"message": "invalid password"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            token = Token.objects.get_or_create(user=user)
            # serializer = UserSerializer(instance=user)
            return Response(
                {"token": str(token[0])},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(str(e))
            return Response(
                data={"message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                headers=get_response_headers()
            )

    def register(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                user = User.objects.get(username=serializer.data['username'])
                user.set_password(serializer.data['password'])
                user.save()

                token = Token.objects.create(user=user)
                return Response(
                    {"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
            print(request.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(str(e))
            return Response(
                data={"message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                headers=get_response_headers()
            )
