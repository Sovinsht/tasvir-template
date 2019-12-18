from django.db import models
from user_app.models import UserModel

# Create your models here.
class PhotoModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, unique=True)
    photo = models.ImageField(upload_to='upload_pic')
    caption = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    like = models.PositiveIntegerField()
