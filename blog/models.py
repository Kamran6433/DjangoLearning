from django.db import models

# Create your models here.
class MinecraftUser(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    minecraft_user = models.ForeignKey(MinecraftUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=3000)
    removeable = models.BooleanField()

    def __str__(self):
        return self.text