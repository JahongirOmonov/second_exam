from django.shortcuts import render
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Vacancy, Category
from .serializers import VacancySerializer, CategorySerializer
from rest_framework import generics
from .models import Resume


@method_decorator(cache_page(60*15), name='dispatch')
class VacancyCompanyResumeListApiView(generics.ListAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    def get(self, request, *args, **kwargs):
        vacancy_count = self.get_queryset().count()
        company_count = Vacancy.objects.all().values('company__title').distinct().count()
        resume_count = Resume.objects.all().count()
        print(company_count)
        return Response({'vacancy_count': vacancy_count, 'company_count':company_count, 'resume_count':resume_count})


@method_decorator(cache_page(60*15), name='dispatch')
class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        category_count = Vacancy.objects.all().values('category__title').distinct().count()
        print(vacancies[0].price_from)
        print(category_count)

        min_and_max = {}
        for i in range(category_count):
            min = 99999
            max = 0
            for vacancy in vacancies:
                print(vacancy.category.id)
                if vacancy.category.id == i+1:
                    if vacancy.price_from < min:
                        min = vacancy.price_from # min = 1 ta vakansiyaning  minimum narxi
                        print("min", min)
                    if vacancy.price_to > max:
                        max = vacancy.price_to  # max =  va xuddi shu vakansiyaning maximum narxi teng
                        print("max", max)
            min_and_max.setdefault(min, max) # har bir vakansiyaning "price_from" va "price_to" si alohida dictga yuklab olindi
            print(min_and_max)
        average_list=[]
        for min, max in min_and_max.items():
            average_list.append((min+max)/2)  #har bir vakansiyaning o'rtacha narxlari "average_list"ga yuklab olindi
        print(">>>>>>>")
        print(average_list)
        print("<<<<<<<<")
        overall_price=[]
        index=0 # bu har bir vakansiyani forda aylantirganda ushlab olish uchun qilindi
        for min,max in min_and_max.items():
            if max >= min * 2:
                overall_price.append(f"{(min+average_list[index])/2} - {(average_list[index]+max)/2} UZS")
                index += 1
            else:
                overall_price.append(f"{average_list[index]} UZS")
                index += 1
        print(overall_price)
        result = []
        category = Vacancy.objects.all().values('category__title').distinct()
        for i in range(len(overall_price)):
            vacancy_amount = Vacancy.objects.filter(category__id=i+1).count()
            info = {
                "Category": category[i]['category__title'],
                "salary": overall_price[i],
                "free_vacancy": vacancy_amount
            }
            result.append(info) # barcha so`ralgan ma`lumotlar dictda yaratilib, so'ngra listga
                                           # joylandi. Maqsad responsega Json korinishda yuborish
        return Response(result)
    # ushbu noqulaychilik uchun uzr. Hayolimga kelgan yo`l shu bo`ldi.


@method_decorator(cache_page(60*15), name='dispatch')
class VacanciesListApiView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


