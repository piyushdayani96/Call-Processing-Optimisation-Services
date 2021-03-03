from django.db import models

class Notification(models.Model):
    notificationtext=models.TextField()
    posteddate=models.CharField(max_length=30)
class Knowledgebase(models.Model):
    problemid=models.CharField(max_length=20)
    problemtext=models.TextField(max)
    solutiontext=models.TextField()
    posteddate=models.CharField(max_length=30)

# Create your models here.
