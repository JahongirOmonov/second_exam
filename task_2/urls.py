from django.urls import path
from .views import VacancyList

urlpatterns = [
    path('vacancies/', VacancyList.as_view()),
]
