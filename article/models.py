# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):

    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Type(models.Model):

    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Text(models.Model):
    title = models.CharField(max_length = 255)
    url = models.URLField(max_length=250, blank=True)
    image1 = models.ImageField(upload_to="static/image/", blank=True)
    image2 = models.ImageField(upload_to="static/image/", blank=True)
    image3 = models.ImageField(upload_to="static/image/", blank=True)
    uploadtime = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank = True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)
    enable = models.BooleanField(default=False)
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)

    def __str__(self):
    	return self.title


class Favorite(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.ForeignKey(Text, on_delete=models.CASCADE)

	class Meta:

		ordering = ('user', 'text')


class Comment(models.Model):
    text = models.ForeignKey(Text, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(blank=True)

    def __str__(self)
        return '%s %s' % (self.text.title, self.user.username)



