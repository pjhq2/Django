from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User


def board_image_path(instance, filename):
    return f'user_{instance.user.pk}/{filename}/'


class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # writer = models.ForeignKey(get_user_model(), verbose_name='작성자', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='original', blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}) {self.title}'