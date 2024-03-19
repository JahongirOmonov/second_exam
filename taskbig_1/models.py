from django.db import models
from utils.models import BaseModel
from utils.choices import Type, TypeOfWork, WorkingTime
from users.models import User
# Create your models here.


class Region(BaseModel):
    title = models.CharField(max_length=31)

    def __str__(self):
        return self.title


class District(BaseModel):
    title = models.CharField(max_length=31)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="districts")

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=31)

    def __str__(self):
        return self.title


class Company(BaseModel):
    title = models.CharField(max_length=31)
    image = models.ImageField(upload_to='images/jobhunt/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Vacancy(BaseModel):
    title = models.CharField(max_length=31)
    description = models.CharField(max_length=31)
    experience = models.CharField(max_length=31, choices=Type.choices, default=Type.INEXPERIENCED)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='vacancies')
    typeOfWork = models.CharField(max_length=7, choices=TypeOfWork.choices,
                                  default=TypeOfWork.OF)
    workingTime = models.CharField(max_length=10, choices=WorkingTime.choices,
                                   default=WorkingTime.FULL)



    price_from = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_to = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    career = models.CharField(max_length=31, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name="jobs")

    def __str__(self):
        return self.title


class Resume(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='resume_user')
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                               related_name='resume_region')
    district = models.ForeignKey(District, on_delete=models.CASCADE,
                                 related_name='resume_district')
    description = models.TextField()
    phone_number = models.CharField(max_length=7)
    email = models.EmailField(blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='resume_category')
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_education = models.BooleanField(default=False)
    is_have_experience = models.BooleanField(default=False)
    is_have_foreign_language = models.BooleanField(default=False)
    is_have_certification = models.BooleanField(default=False)
    is_have_driver_license = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username







