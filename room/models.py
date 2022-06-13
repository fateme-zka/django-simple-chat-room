from django.db import models
from django.utils.text import slugify

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  # it's for the url for each room

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)
