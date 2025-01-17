from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.subject


#==================================================
class UserScore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Score: {self.score}"
