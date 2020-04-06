from django.db import models


# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=50)
    bio = models.TextField()
    task_name = models.CharField(max_length=50)
    task_desc = models.TextField()
    created = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='Images/', default="Images/None/noimg.jpg")
