from django.db import models



class Food(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    picture=models.ImageField(null=True)


    def __str__(self):
        return self.name
