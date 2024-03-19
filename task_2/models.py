from django.db import models
from utils.models import BaseModel

# Create your models here.


class Vacancy(BaseModel):
    title = models.CharField(max_length=31)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_from = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

