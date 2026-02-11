from rest_framework import serializers
from tags.models import Tags

class WriteTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name', 'slug')

class ReadTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name', 'slug', 'created_at', 'updated_at')