from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.throttling import UserRateThrottle

class SimplePaginationClass(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5

class OtherPaginationClass(LimitOffsetPagination):
    default_limit = 2
    max_limit = 5

class MyUserRateThrottleClass(UserRateThrottle):
    # custom throttle class
    rate = "25/hour" # min/hour/day