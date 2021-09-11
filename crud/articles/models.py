from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail, ResizeToFill, ResizeToFit


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to='original',
        blank=True,
        processors=[ResizeToFit(500, 500), ],
        format='JPEG',
        options={'quality': 100, },
    )
    thumbnail_image = ImageSpecField(
        source='image',
        processors=[Thumbnail(100, 100), ],
        format='JPEG',
        options={'quality': 60, },
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    