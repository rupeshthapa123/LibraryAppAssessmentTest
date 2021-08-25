from django.db import models

class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to ='images')
    author = models.CharField(max_length = 50, default='Anonymous')
    describe = models.TextField(default = 'Description')

    def __str__(self):
        return self.name