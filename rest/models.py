from django.db import models

# Create your models here.
class Article(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    department=models.CharField(max_length=50)
    salary=models.IntegerField()
    city=models.TextField()
    Jobdescription=models.CharField(max_length=100,null=False)
    joined=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name


