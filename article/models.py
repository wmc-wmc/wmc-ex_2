from django.db import models

# Create your models here.
class Text(models.Model):
    title = models.CharField(max_length = 255)
    source = models.TextField(max_length = 255)
    image = models.ImageField(upload_to="image/")
    uploadtime = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank = True)
