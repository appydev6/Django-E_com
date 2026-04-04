from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class SimplePaginationClass(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5

class OtherPaginationClass(LimitOffsetPagination):
    default_limit = 2
    max_limit = 5