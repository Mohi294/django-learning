from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)#auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #if a user is deleted the post will be deleted but not in apoosit wat for deletion of post
    
    def __str__(self):
        return self.title
