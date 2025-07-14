from django.db import models
from django.utils import timezone

class Contact(models.Model):
    sender = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    receiver = models.EmailField()
    subject = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message from {self.sender} - {self.subject} to {self.receiver}"
