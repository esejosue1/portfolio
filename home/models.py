from django.db import models

# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=50, unique=True)
    description=models.TextField(max_length=500)
    projectImg=models.ImageField(upload_to="images/projects", blank=True)
    link=models.CharField(max_length=250)

    def __str__(self):
        return self.title
