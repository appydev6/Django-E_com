from tags.views import (
    CreateTagViewV1, CreateTagViewV2, TagListViewV1, TagListViewV2, TagDetailViewV1, TagDetailViewV2,
    DeleteTagView1, DeleteTagView2, DeleteAllTagsView
    )
from django.urls import path

urlpatterns = [
    path('create/v1/', CreateTagViewV1.as_view(), name='create-tag-v1'),
    path('create/v2/', CreateTagViewV2.as_view(), name='create-tag-v2'),
    path('tag-list/v1/', TagListViewV1.as_view(), name='tag-list-v1'),
    path('tag-list/v2/', TagListViewV2.as_view(), name='tag-list-v2'),
    path('tag-detail/v1/<str:slug>', TagDetailViewV1.as_view(), name='tag-detail-v1'),
    path('tag-detail/v2/<str:slug>', TagDetailViewV2.as_view(), name='tag-detail-v2'),
    path('tag-delete/v1/<str:slug>', DeleteTagView1.as_view(), name='tag-delete-v1'),
    path('tag-delete/v2/<str:slug>', DeleteTagView2.as_view(), name='tag-delete-v2'),
    path('all-tags-delete/', DeleteAllTagsView.as_view(), name='all-tags-deleted'),
]
