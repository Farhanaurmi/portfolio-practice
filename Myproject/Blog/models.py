from django.db import models

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=150)
    date=models.DateField()
    description=models.TextField()

    def __str__(self):
        return self.title