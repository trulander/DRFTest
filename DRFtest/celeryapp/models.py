from django.db import models

class CeleryModel(models.Model):

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name