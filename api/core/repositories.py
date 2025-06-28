from .models import (
    Employee
)

class EmployeeRepository:
    def create(self, data):
        return Employee.objects.create(**data)
