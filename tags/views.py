from rest_framework import views, status
from rest_framework.response import Response
from tags.serializers import WriteTagSerializer, ReadTagSerializer
from tags.models import Tags
from django.utils.text import slugify
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView

class CreateTagViewV1(APIView):
    def post(self, request):
        serializer = WriteTagSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')    #'validated_data' has to be called after the 'is_valid' only (or) else if it is called directly it will through an error.
            tag_object = Tags.objects.create(name=name, slug=slugify(name))
            response_data = ReadTagSerializer(instance=tag_object).data
            return Response(response_data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateTagViewV2(CreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = WriteTagSerializer

class TagListViewV1(APIView):
    def get(self, request):
        tag_objects = Tags.objects.all()
        response_data = ReadTagSerializer(instance=tag_objects, many=True).data
        if response_data:
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({"message" : "No Tags to show"}, status=status.HTTP_204_NO_CONTENT)

class TagListViewV2(ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = ReadTagSerializer

class TagDetailViewV1(APIView):
    def get(self, request, slug):
        try:
            tag_object = Tags.objects.get(slug=slug)
            response_data = ReadTagSerializer(instance=tag_object).data
            return Response(response_data, status=status.HTTP_200_OK)
        except (Tags.DoesNotExist, Tags.MultipleObjectsReturned):
            return Response({"message" : "Tag does not exist"}, status=status.HTTP_400_BAD_REQUEST)

class TagDetailViewV2(RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class = ReadTagSerializer
    lookup_field = "slug"

class DeleteTagView1(APIView):
    def delete(self, request, slug):
        try:
            tag_object = Tags.objects.get(slug=slug)
            tag_object.delete()
            return Response({"message" : "Tag deleted"}, status=status.HTTP_200_OK)
        except (Tags.DoesNotExist, Tags.MultipleObjectsReturned):
            return Response({"message" : "Tags does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteTagView2(DestroyAPIView):
    queryset = Tags.objects.all()
    lookup_field = "slug"

class DeleteAllTagsView(APIView):
    def delete(self, request):
        queryset = Tags.objects.all()
        if queryset:
            deleted_count, _ = queryset.delete()
            return Response({"message": f"All {deleted_count} tags deleted"}, status=status.HTTP_200_OK)
        else:
            return Response({"message" : "Empty"}, status=status.HTTP_400_BAD_REQUEST)

        
