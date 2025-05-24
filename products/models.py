from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class product(models.Model):
    title = models.CharField(max_length=120,)
    price = models.FloatField(default=10)
    catagory = models.ForeignKey(category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
