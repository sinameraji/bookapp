from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    review = models.TextField()
    #coverImage = models.ImageField(upload_to = 'images')
    readDate = models.DateField(
        blank=True, null=True)

    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.title