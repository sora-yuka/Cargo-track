from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from applications.profiles.models import CompanyProfile, DriverProfile

User = get_user_model()


class CRating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cratings')
    worker = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='cratings')
    rating = models.SmallIntegerField(
        validators= [
        MinValueValidator(1),
        MaxValueValidator(10)
        ], blank=True, null= True
    )
    
    def __str__(self) -> str:
        return f'{self.owner} - {str(self.rating)}'
    

class DRating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dratings')
    worker = models.ForeignKey(DriverProfile, on_delete=models.CASCADE, related_name='dratings')
    rating = models.SmallIntegerField(
        validators= [
        MinValueValidator(1),
        MaxValueValidator(10)
        ], blank=True, null= True
    )
    
    def __str__(self) -> str:
        return f'{self.owner} - {str(self.rating)}'