from django.db import models
from .managers import UserManager


class Profile(models.Model):
    name = models.CharField(max_length=31)
    surname = models.CharField(max_length=31)
    date_of_birth = models.DateField()
    is_deleted = models.BooleanField(default=False)
    objects = UserManager()
    all_objects = models.Manager()

    def soft_deleted(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    def __str__(self):
        return self.name






