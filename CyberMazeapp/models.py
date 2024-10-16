from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.subject
