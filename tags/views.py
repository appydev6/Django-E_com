from rest_framework import views, status
from rest_framework.response import Response
from tags.serializers import WriteTagSerializer, ReadTagSerializer
from tags.models import Tags
from django.utils.text import slugify

class CreateTagView(views.APIView):
    def post(self, request):
        serializer = WriteTagSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            #'validated_data' has to be called after the 'is_valid' only 
            # (or) else it will if it is called directly it will through an error.
            tag_object = Tags.objects.create(name=name, slug=slugify(name))
            response_data = ReadTagSerializer(instance=tag_object).data
            return Response(response_data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        