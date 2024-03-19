from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Vacancy
from .serializers import VacancySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class VacancyList(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('salary',)
    filterset_fields = ('salary',)

    def get_queryset(self):
        queryset = super().get_queryset()
        less = self.request.query_params.get('less')
        much = self.request.query_params.get('much')
        if less:
            queryset = queryset.filter(salary_from__gte=less)
        if much:
            queryset = queryset.filter(salary_to__lte=much)
        return queryset
