from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)



    def save(self, *args, **kwargs):
        existing_user = User.objects.filter(
            Q(username=self.username) | Q(email=self.email)
        ).first()

        if existing_user:
            message = f"{existing_user.username} or {existing_user.email} is already taken"
            raise ValidationError(message)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


    class Meta:
        verbose_name_plural = "Users"
