from django.db import models
from django.contrib.auth.models import AbstractUser


class Address(models.Model):
    street_address1 = models.CharField(max_length=255)
    street_address2 = models.CharField(max_length=255)


class StaffBase(AbstractUser):
    base = models.CharField(max_length=100)

    def get_role(self):
        return self.company_role

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

class Intern(models.Model):
    mentor = models.ForeignKey("Manager", related_name="interns", on_delete=models.CASCADE)
    internship_end = models.DateTimeField(auto_now_add=True)

