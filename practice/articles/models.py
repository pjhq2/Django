from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField

class Article(models.Model):
    title = CharField(max_length=28)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)