from rest_framework import serializers
from products.models import Product
from tags.serializers import ReadTagForProductSerializer, ReadTagSerializer

# Create your serializers here.
class WriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'description', 'tags', 'price', 'quantity', 'image']

class ReadProductSerializer(serializers.ModelSerializer):

    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_tags(self, Product):
        product_tags = Product.tags.all().only("id", "name", "slug")
        # tag_names = [tag['name'] for tag in product_tags]
        return ReadTagForProductSerializer(instance= product_tags, many=True).data
        # product_tags = Product.tags.all()
        # return ReadTagSerializer(instance= product_tags, many=True).data
