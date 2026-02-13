from tags.views import CreateTagView
from django.urls import path

urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create-tag')
]