from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .models import *
from .servece import *


class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'sucess': "Hurray you are authentic"})


class ProductView(APIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get(self, request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category__category_name = category)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        return Response({'count': len(serializer.data), 'data': serializer.data})

# class ProductView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = ProductFilter





