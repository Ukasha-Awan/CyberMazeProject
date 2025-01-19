from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.subject

class UserScore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    result = models.CharField(max_length=10, default='fail')  # 'pass' or 'fail'
    level = models.IntegerField(default=1)

# class Supervisor(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to="supervisor_images/")
#     phone_number = models.CharField(max_length=15)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

# class Team(models.Model):
#     supervisor = models.ForeignKey(on_delete=models.CASCADE)
#     student1 = models.ForeignKey(
#         Student, related_name="student1", on_delete=models.CASCADE
#     )
#     student2 = models.ForeignKey(
#         Student, related_name="student2", on_delete=models.CASCADE
#     )
#     student3 = models.ForeignKey(
#         Student, related_name="student3", on_delete=models.CASCADE, null=True
#     )
#     project_title = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return f"Team {self.project_title}"



