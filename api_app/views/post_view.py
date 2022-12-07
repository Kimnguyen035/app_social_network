from .views import *

class PostView(ViewSet):
    
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
        return response_data(message=ERROR['not_exists_post'])
    
    def post_blog(self, request):
        data = request.data.copy()
        data_save = PostSerializer(data=data)
        if not data_save.is_valid():
            return validate_error(message=data_save.errors)
        data_save.save()
        return response_data(data_save.data)
    
    def edit_post(self, request, id):
        data = request.data.copy()
        status, data_id = self.get_post_data(id)
        if not status:
            return response_data(message=ERROR['not_exists_post'],status=STATUS['NO_DATA'])
        queryset = Post.objects.get(id=id)
        data_save = PostSerializer(queryset, data=data, partial=True)
        if not data_save.is_valid():
            return validate_error(message=data_save.errors)
        data_save.save()
        return response_data(data_save.data)
    
    def delete_post(self, request, id):
        data = request.data.copy()
        status, data_id = self.get_post_data(id)
        if not status or data_id['deleted_at'] is not None:
            return response_data(message=ERROR['not_exists_post'],status=STATUS['NO_DATA'])
        delete_post = Post.objects.get(id=data_id['id'])
        delete_post.deleted_at = datetime.now()
        delete_post.save()
        return response_data(message=ERROR['deleted_post'])