
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.AgentListPlainView.as_view()),
    path('products-encrypted/', views.ProductListEncryptedView.as_view()),
    path('products-decrypt/', views.DecryptProductList.as_view())
]
