from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
from taggit.managers import TaggableManager
#from artists.models import Artist

class Music_Class(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    full_description = models.TextField()
    artist = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    genres = TaggableManager()
    viewer = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        if len(self.title) > 25:
            return self.title[:25] + "..."
        else:
            return self.title

class Comment(models.Model):
    article = models.ForeignKey(Music_Class, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(max_length=3000)
    writer = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.writer) + " " + str(self.id)
#
    