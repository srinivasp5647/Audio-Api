from django.db import models

# Create your models here.

class SongFiles(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PodCastFiles(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    host = models.CharField(max_length=100)
    participants = models.CharField(max_length=100, null=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AudioBookFiles(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title