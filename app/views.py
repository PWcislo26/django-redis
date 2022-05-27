from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.core.cache import cache

# Create your views here.


class ProductList(APIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    serializer_class = ProductSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = cache.get(pk)
        if product is not None:
            print("data from cache")
        else:
            product = self.get_object(pk)
            print("data from database")
            cache.set(pk, product)
        serializer = ProductSerializer(product)
        return Response(serializer.data)