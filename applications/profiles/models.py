from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile/images/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    def generate_default_username(self):
        return f"{self.user.id}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = "User000" + self.generate_default_username()
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return str(self.user.email)