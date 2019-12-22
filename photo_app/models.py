from django.db import models
from user_app.models import UserModel

# Create your models here.
class PhotoModel(models.Model):
    uploaded_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='uploaded_posts')
    photo = models.ImageField(upload_to='upload_pic')
    caption = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    like = models.PositiveIntegerField()


      
class CommentModel(models.Model):
    Comment = models.TextField()
    comment_by = models.ForeignKey(UserModel, on_delete=models.CASCADE,related_name='comments')
    parentpost = models.ForeignKey(PhotoModel, on_delete=models.CASCADE,related_name='comments')
    timestamp1 = models.DateTimeField(auto_now=True)
