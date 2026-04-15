from rest_framework import views, status
from rest_framework.response import Response
from tags.serializers import WriteTagSerializer, ReadTagSerializer
from tags.models import Tags
from django.utils.text import slugify
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from authentication.permissions import IsAdmin
from django.core.cache import cache

# Create your views here.
# flow: request.data → Serializer → validated_data → Manual ORM create → ReadSerializer → 200 OK
class CreateTagViewV1(APIView):
    
    permission_classes = (IsAdmin, )
    
    def post(self, request):
        serializer = WriteTagSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name") # type: ignore
            #'validated_data' has to be called after the 'is_valid' only 
            # (or) else if it is called directly it will through an error.
            
            tag_object = Tags.objects.create(name=name, slug=slugify(name)) # type: ignore
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
    
    # given a slug, try finding that tag with that slug in the cache
    # if the tag is in the cache:
    #     return the cached tag
    # else:
    #     generate the tag
    #     save the generated tag in the cache (for next time)
    #     return the generated tag
    def fetch_tag_from_cache(self,cache_key):
        return cache.get(cache_key)

    def get(self, request, slug):
        try:
            cache_key = f"tag_{slug}"
            tag_from_cache = self.fetch_tag_from_cache(cache_key)
            if tag_from_cache is not None:
                print("Tag data coming from cache")
                return Response(tag_from_cache)
            tag_object = Tags.objects.get(slug=slug)
            response_data = ReadTagSerializer(instance=tag_object).data
            cache.set(cache_key, response_data)
            print("Fetching tag from the db for the first time and storing it in the cache for the next time.")
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

        
