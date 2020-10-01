from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=30)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    marital_status = models.CharField(max_length=30)
    
