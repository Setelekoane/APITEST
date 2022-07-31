from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100,blank=True, default='')
    body=models.TextField()
    created_at=models.DateField(auto_now_add=True)


    class Meta:
        ordering=['created_at']
        

