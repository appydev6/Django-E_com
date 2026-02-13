from tags.views import CreateTagView, TagDetailViewV1, TagDetailViewV2
from django.urls import path

urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create-tag'),
    path('tag-detail/v1/<str:slug>', TagDetailViewV1.as_view(), name='tag-detail-v1'),
    path('tag-detail/v2/<str:slug>', TagDetailViewV2.as_view(), name='tag-detail-v2'),
]