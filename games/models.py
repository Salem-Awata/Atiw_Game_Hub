from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    cover_image_url = models.URLField(blank=True, null=True)
    template_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title
