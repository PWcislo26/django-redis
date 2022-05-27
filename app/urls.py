from django.urls import path, include
from .views import ProductList, ProductDetail
app_name = 'app'

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
]
