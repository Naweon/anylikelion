from django.db import models
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
    title = models.TextField(max_length=200)
    body = models.TextField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title