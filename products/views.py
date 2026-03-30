from products.models import Product
from django.utils.text import slugify
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from products.serializers import WriteProductSerializer, ReadProductSerializer

# Create your views here.
# flow: request.data → Add slug → Serializer → validated_data → serializer.save() → ReadSerializer → 201 CREATED
class CreateProductView(APIView):
    def post(self, request):
        request_data = request.data
        request_data.update({'slug' : slugify(request_data.get('name'))})
        serializer = WriteProductSerializer(data=request_data)
        if serializer.is_valid():
            product_instance = serializer.save()
            response_data = ReadProductSerializer(instance= product_instance).data
            return Response(response_data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ReadProductSerializer

