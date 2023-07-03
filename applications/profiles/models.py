from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from applications.car.models import CarInfo

# Create your models here.


User = get_user_model()


class BaseProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=155, null=True, blank=True)
    last_name = models.CharField(max_length=155, null=True, blank=True)
    phone = PhoneNumberField()
    billing_address = models.CharField(max_length=155, null=True, blank=True)
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
    

class ShipperProfile(BaseProfile):
    role = models.CharField(max_length=55, default="shipper")
    
    def __str__(self):
        return self.user.email
    

class DriverProfile(BaseProfile):
    mc_dot_number = models.CharField(max_length=10, null=True, blank=True)
    role = models.CharField(max_length=55, default="driver")
    car = models.ForeignKey(CarInfo, on_delete=models.CASCADE, related_name="driver_car")
    
    def __str__(self):
        return self.user.email
    
    
class CompanyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company_profile")
    company = models.CharField(max_length=155, null=True, blank=True)
    registration_number = models.CharField(max_length=30, null=True, blank=True)
    company_license = models.TextField(null=True, blank=True)
    company_license_file = models.FileField(upload_to=f"company license/license/{company}/", null=True, blank=True)
    insurance_contract = models.TextField(null=True, blank=True)
    insurance_contract_file = models.FileField(upload_to=f"campany contract/contract/{company}/", null=True, blank=True)
    billing_address = models.CharField(max_length=155, null=True, blank=True)
    mc_dot_number = models.CharField(max_length=10, null=True, blank=True)
    auto_park = models.ForeignKey(CarInfo, on_delete=models.CASCADE, related_name="company_autopark")