from django.db import models
from .post import Post

class Img(models.Model):
    class Meta:
        db_table = 'image'
    id = models.AutoField(primary_key=True)
    image = models.ForeignKey(Post, related_name='image_post', on_delete=models.CASCADE)
    src_image = models.TextField()
    status_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()