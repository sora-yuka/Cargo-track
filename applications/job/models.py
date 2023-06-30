from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Job(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    pickup_location = models.CharField(max_length=200)
    pickup_date = models.CharField(max_length=100)
    delivery_date = models.CharField(max_length=100)
    destination_location = models.CharField(max_length=200)
    weight_of_goods = models.CharField(max_length=100)
    type_of_goods = models.CharField(max_length=100)
    required_equipment = models.CharField(max_length=200)
    special_instruction = models.TextField(null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.title
    
    
    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
    
    