from django.db import models


class Type(models.TextChoices):
    INEXPERIENCED = 'Inexperienced', 'Inexperienced'
    BETWEEN_1_AND_3 = 'Between 1 and 3 years', 'Between 1 and 3 years'
    BETWEEN_3_AND_6 = 'Between 3 and 6 years', 'Between 3 and 6 years'
    MORE_6 = 'More 6 years', 'More 6 years'
    UNIMPORTANT = 'Unimportant', 'Unimportant'


class TypeOfWork(models.TextChoices):
    OF = "OFF", 'offline'
    ON = "ON", 'online'

class WorkingTime(models.TextChoices):
    FULL = "FULL", 'Full time'
    HALF = "HALF", 'Half day'
