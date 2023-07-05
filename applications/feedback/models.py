from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from applications.profiles.models import BaseProfile

User = get_user_model()


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    worker = models.ForeignKey(BaseProfile, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(
        validators= [
        MinValueValidator(1),
        MaxValueValidator(10)
        ], blank=True, null= True
    )
    
    def __str__(self) -> str:
        return f'{self.owner} - {str(self.rating)}'