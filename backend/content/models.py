from django.db import models

# Create your models here.
class ContentItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='content_images/')

    def __str__(self):
        return self.title