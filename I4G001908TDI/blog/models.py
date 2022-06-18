from django.db import models
# from django.conf import settings

from django.contrib.auth import get_user_model

# Create your models here.



class Post(models.Model):
       title = models.CharField(max_length=200)
       text = models.TextField()
       author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
       created_date =models.DateTimeField('date created')
       published_date = models.DateTimeField('date published')
       # pass
       
       def __str__(self) -> str:
              return self.title