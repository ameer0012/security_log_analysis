# Create your models here.
from django.db import models


class LogEvent(models.Model):
    timestamp = models.DateTimeField(),
    level = models.CharField(max_length=50),
    user_id = models.IntegerField(null=True),
    user_name = models.CharField(max_length=100, null=True),
    user_email = models.EmailField(null=True),
    tags = models.TextField(null=True),
    source = models.CharField(max_length=100),
    objects = models.Manager(),
    message = models.TextField()

    def __str__(self):
        return f"LogEvent: {self.timestamp} - {self.level}"
