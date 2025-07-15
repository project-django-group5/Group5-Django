from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.auth.models import User

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_given')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_received')
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer.username} → {self.receiver.username} : {self.rating}"

    class Meta:
        unique_together = (('reviewer', 'receiver', 'skill'),)
>>>>>>> 9e8f17c89ae934e7c13571a9db77a0d7a0d9fb2e
