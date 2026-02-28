from django.shortcuts import render
from products.serializers import WriteProductSerializer
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class CreateProductView(APIView):
    
    def post(self, request):
        request_data = request.data
        request_data.update({'slug' : slugify(request_data.get('name'))})
        serializer = WriteProductSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)