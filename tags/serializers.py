from rest_framework import serializers
from tags.models import Tags

# types of serializer by name
# read serilizer is used to read operations of DB
# write serilizer is user to write operations of DB

class WriteTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name',)
        # Single-item tuple (needs trailing comma) 
        # because The `fields` option must be a list or tuple or "__all__".

class ReadTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name', 'slug', 'created_at', 'updated_at')