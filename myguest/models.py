from django.db import models

# Create your models here.

class Guest(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    class Meta:
        ordering  = ('-id',)
    
    
    