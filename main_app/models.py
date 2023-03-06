from django.db import models

# Create your models here.

class Finch (models.Model):
    
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

# After creating a model we need to make migrations and then if we need to,
# we can do show migrations and then migrate the model. 

    def __str__(self):
     return self.name