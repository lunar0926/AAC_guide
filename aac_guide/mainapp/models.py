from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    category_name = models.CharField(max_length=10)


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=30)
    post_content = models.TextField()
    post_image = models.ImageField(upload_to='mainapp', null=True)
    post_created_at = models.DateTimeField(auto_now_add=True)