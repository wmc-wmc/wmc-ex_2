# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Text(models.Model):
    title = models.CharField(max_length = 255)
    url = models.URLField(max_length=250, blank = True)
    image = models.ImageField(upload_to="static/image/", blank = True)
    uploadtime = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank = True)
    subject = models.CharField(max_length = 20)
    enable = models.BooleanField(default=False)
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)

    def __str__(self):
    	return self.title


class Favorite(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.ForeignKey(Text, on_delete=models.CASCADE)

	class Meta:

		ordering = ('user', 'text')
