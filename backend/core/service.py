from .repositories import (
    EmployeeRepository
)

class EmployeeService:
    def __init__(self):
        self.repository = EmployeeRepository()

    def create_employee(self, data):
        return self.repository.create(data)