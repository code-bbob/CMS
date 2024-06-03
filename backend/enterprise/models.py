from django.db import models
from repair.models import Repair

# Create your models here.

class Enterprise(models.Model):
    name = models.CharField(max_length=40)
    repairs = models.ManyToManyField(Repair, related_name="enterprise_repairs", blank=True)#related name uta reverse relation query ma pani use hunxa 
    
    def __str__(self):
        return self.name