from .views import *
from ..tasks import *

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
        post_save = PostValueValidate(data=data)
        if not post_save.is_valid():
            return validate_error(post_save.errors, STATUS['INPUT_INVALID'])
        # create_blog.delay(post_save.data)
        # create_blog.apply_async(kwargs={'value':post_save.data})
        add.apply_async(('q','q'), link_error=error_handler.s())
        return response_data(message=SUCCESS['create_post'], data=post_save.data)
    
    def edit_post(self, request, id):
        data = request.data.copy()
        status, data_id = self.get_post_data(id)
        if not status:
            return response_data(message=ERROR['not_exists_post'],status=STATUS['NO_DATA'])
        queryset = Post.objects.get(id=data_id['id'])
        data_save = PostSerializer(queryset, data=data, partial=True)
        if not data_save.is_valid():
            return validate_error(data_save.errors, STATUS['FAIL_REQUEST'])
        data_save.save()
        return response_data(message=SUCCESS['update_post'], data=data_save.data)
    
    def delete_post(self, request, id):
        data = request.data.copy()
        status, data_id = self.get_post_data(id)
        if not status or data_id['deleted_at'] is not None:
            return response_data(message=ERROR['not_exists_post'],status=STATUS['NO_DATA'])
        delete_post = Post.objects.get(id=data_id['id'])
        delete_post.deleted_at = datetime.now()
        delete_post.save()
        return response_data(message=SUCCESS['deleted_post'])
    
    def get_trash(self, request):
        queryset = Post.objects.exclude(deleted_at__isnull=True)
        serializer = PostSerializer(queryset, many=True)
        return response_data(data=serializer.data)
    
    def restore_post(self, request):
        data = request.data.copy()
        status, data_id = self.get_post_data(id)
        if not status or data_id['deleted_at'] is None:
            return response_data(message=ERROR['not_exists_trash'],status=STATUS['NO_DATA'])
        delete_post = Post.objects.get(id=data_id['id'])
        delete_post.deleted_at = datetime.now()
        delete_post.save()
        return response_data(message=SUCCESS['restore_post'])
    
    def drop_post(self, request, id):
        data = request.GET.copy()
        status, data_id = self.get_post_data(id)
        if not status:
            return response_data(message=ERROR['not_exists_post'],status=STATUS['NO_DATA'])
        Post.objects.get(id=data_id['id']).delete()
        return response_data(message=SUCCESS['drop_post'])