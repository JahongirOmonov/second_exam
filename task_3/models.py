from utils.models import BaseModel
from django.db import models


class Product(BaseModel):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    marja = models.DecimalField(max_digits=10, decimal_places=2)
    package_code = models.CharField(max_length=31)

