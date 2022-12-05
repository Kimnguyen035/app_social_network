from .views import *
# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class PostView(ViewSet):
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # http_method_names = ['post']
    
    def all_post(self, request):
        queryset = Post.objects.filter(deleted_at__isnull=True)
        paginator = StandardPagination()
        pagination = paginator.paginate_queryset(queryset=queryset, request=request)
        serializer = PostSerializer(pagination, many=True, fields=['id', 'title', 'content'])
        return response_paginator(queryset.count(), paginator.page_size, serializer.data)
    
    def get_post_data(self, id):
        validate = IdGetPostValidate(data={'id':id})
        if not validate.is_valid():
            return False, validate.errors
        return True, validate.data['data']
    
    def detail_post(self, request, id):
        status, data = self.get_post_data(id)
        if status:
            return response_data(data)
        return validate_error(data)
    
    def edit_post(self, request):
        data = request.data.copy()
        
        return response_data()