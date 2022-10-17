from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField('タイトル', max_length=200)
  text = models.TextField('内容')
  created = models.DateTimeField('作成日', default=timezone.now())
  
  def __str__(self):
    return self.title
  
