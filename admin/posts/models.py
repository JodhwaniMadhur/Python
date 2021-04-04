from django.db import models

# Create your models here.
class Post(models.Model):#step 4
    text=models.TextField()

    def __str__(self):
        return self.text[:50]
