from django.db import models

class Feedback(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    message = models.TextField()
    author = models.CharField(max_length=100, blank=True, default='')
    rate = models.IntegerField(blank=False, default=10)

    class Meta:
        ordering = ('-rate', '-created')
