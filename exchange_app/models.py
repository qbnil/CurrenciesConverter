from django.db import models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=3, unique=True)
    rate = models.FloatField(null=False, blank=False, default=0.0)

    def __str__(self):
        return f"{self.name} ({self.rate})"