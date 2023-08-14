from django.db import models

# Create your models here.

class PM(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    contact_no = models.CharField(max_length=10)
    
    def __str__(self):
        return self.fname+ " " +self.lname