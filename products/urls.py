from django.urls import path
from products.views import CreateProductView, ProductListView

urlpatterns = [
    path('create/', CreateProductView.as_view(), name='create-product'),
    path('list-products/', ProductListView.as_view(), name='list-product'),
]