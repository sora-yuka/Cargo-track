import random
import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Job(models.Model):
    
    STATUS = (
        ('Looking for shipper', 'Looking for shipper'),
        ('Loading goods', 'Loading goods'),
        ('Delivering', 'Delivering'),
        ('Completed', 'Completed'),
    )
    
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
    driver_id = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default='Looking for shipper')
    activation_code = models.UUIDField(default=uuid.uuid4())
    complete_code = models.UUIDField(default=uuid.uuid4())
    cancel_code = models.UUIDField(default=uuid.uuid4())
    started_at = models.DateTimeField(null=True, blank=True)
    is_confirm = models.BooleanField(default=False)
    cost = models.CharField(max_length=20, default=random.randint(1000, 4000))
    
    
    def save(self, *args, **kwargs):
        self.cost = str(self.cost) + ' $'
        super().save(*args, **kwargs)
    
    
    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"