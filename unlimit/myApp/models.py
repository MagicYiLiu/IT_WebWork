from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Create form to store the register data
class userData (models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True,null=True)

    class Meta:
        verbose_name_plural = "User data"
