from django.db import models
from django_extensions.db.models import TimeStampedModel
from taggit.managers import TaggableManager


class Image(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name='title')
    file = models.ImageField(verbose_name='image file')
    album = models.ForeignKey('images.Album', blank=True, null=True,
                              verbose_name='album')

    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'


class Album(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name='title')
