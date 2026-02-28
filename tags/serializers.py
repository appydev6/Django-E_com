from rest_framework import serializers
from django.utils.text import slugify
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
    def create(self, validated_data):
        name = validated_data['name']
        slug = slugify(name)
        unique_slug = slug
        counter = 1
        while Tags.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{counter}"
            counter += 1
        validated_data['slug'] = unique_slug
        return super().create(validated_data)

class ReadTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name', 'slug', 'created_at', 'updated_at')