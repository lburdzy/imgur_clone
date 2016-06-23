from django.db import models
from django_extensions.db.models import TimeStampedModel


class Image(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name='title')
    file = models.ImageField(verbose_name='image file')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
