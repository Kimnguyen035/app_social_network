from django.db import models
from ..models.user import User
from ..models.post import Post

class SavePost(models.Model):
    class Meta:
        db_table = 'save_post'
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()