from django.db import models

class Mail(models.Model):
    class Meta:
        db_table = 'mail'
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    from_mail = models.CharField(max_length=255)
    to = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    description = models.CharField(default='unsend',max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()