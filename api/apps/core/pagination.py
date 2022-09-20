from rest_framework.pagination import CursorPagination, PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    """
    普通分页，数据量越大性能越差
    """

    # 默认页面展示的条数
    page_size = 10
    # 前端访问url需要添加 ?page=页码
    page_query_param = "page"
    # 用户自定义返回的条数，格式?size=页数
    page_size_query_param = "size"
    # 用户自定义返回的条数最大限制，数值超过20也只展示20条
    max_page_size = 20


class MyCursorPagination(CursorPagination):
    """
    Cursor 光标分页 性能高，安全
    """

    page_size = 10
    ordering = "-update_time"
    page_size_query_param = "size"
    max_page_size = 20
