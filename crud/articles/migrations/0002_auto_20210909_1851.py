# Generated by Django 3.2.7 on 2021-09-09 09:51

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AddField(
            model_name='article',
            name='image_processed',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]