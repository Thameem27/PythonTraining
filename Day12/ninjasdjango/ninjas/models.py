from django.db import models

# Create your models here.
class Developer(models.Model):
    Name = models.CharField(max_length=200)
    Experience = models.IntegerField(default=0)
    Country = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Name

class Skill(models.Model):
    Skill_name = models.CharField(max_length=200)
    Skill_level = models.CharField(max_length=50)
    Developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Skill_name