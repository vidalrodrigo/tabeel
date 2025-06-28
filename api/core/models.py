from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=254)
    ative = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
