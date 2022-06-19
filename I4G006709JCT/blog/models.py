from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post (models.Model):
   title = models.CharField(max_length=250)
   body_text = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   created_date = models.DateTimeField(auto_now_add=True)
   published_date = models.DateTimeField(auto_now=True)
   

