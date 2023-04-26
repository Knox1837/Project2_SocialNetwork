from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images')
    
class Post(models.Model):
    caption = models.CharField(max_length=1000)
    image = models.FileField(null=True, blank=True, upload_to='images/')
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.caption
    class Meta:
        db_table = 'app_Network'