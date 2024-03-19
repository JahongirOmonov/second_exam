from django.db import models


class UserManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)
