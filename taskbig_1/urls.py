from django.urls import path

from taskbig_1 import views

urlpatterns = [
    path('vacancy-company-resume-count/', views.VacancyCompanyResumeListApiView.as_view()),
    path('categories-vacancy-salary/', views.CategoryListApiView.as_view()),
    path('vacancies/', views.VacanciesListApiView.as_view()),
]
