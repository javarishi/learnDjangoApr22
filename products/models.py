from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2) #999.99
    feedback = models.TextField(blank=True, null=True)
    summary= models.TextField()