from django.db import models

# Create your models here.
class Chat(models.Model):
    question = models.TextField()
    answer = models.TextField()
    title = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)