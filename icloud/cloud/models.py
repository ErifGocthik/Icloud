import datetime
import fileinput

from django.db import models

# Create your models here.

from icloud.settings import DEFAULT_NAME


class Image(models.Model):
    name = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=1020, blank=True, null=True)
    image = models.ImageField(upload_to='%Y/%m/%d', null=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.image.name

class Archive(models.Model):
    title = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='archive_icons/')
    images = models.ManyToManyField(Image, verbose_name='Изображения')

    class Meta:
        ordering = ['id',]