from datetime import datetime

from django.db import models


class ServiceArea(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    description = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
