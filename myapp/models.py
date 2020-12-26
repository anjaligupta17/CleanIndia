from django.db import models

# Create your models here.


class contactModel(models.Model):
    Email = models.CharField(max_length=50)
    Query = models.CharField(max_length=150)

    def __str__(self):
        return self.Email
