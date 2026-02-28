from django.db import models
from tags.models import Tags

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tags, blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.URLField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = "products"
