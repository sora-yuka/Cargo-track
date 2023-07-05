from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from applications.car.models import CarInfo

# Create your models here.

DRIVER_STATUS = (
    ("free", "free"),
    ("busy", "busy"),
)


User = get_user_model()


class BaseProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=155, null=True, blank=True)
    last_name = models.CharField(max_length=155, null=True, blank=True)
    phone = PhoneNumberField(blank=True, null=True)
    billing_address = models.CharField(max_length=155, null=True, blank=True)
    image = models.ImageField(upload_to='profile/images/', null=True, blank=True)
    shipper = models.BooleanField(default=False, blank=True)
    driver = models.BooleanField(default=False, blank=True)
    company_driver = models.BooleanField(default=False, blank=True)
    
    
    def generate_default_username(self):
        return f"{self.user.id}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = "User000" + self.generate_default_username()
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return str(self.user.email)
    

class ShipperProfile(BaseProfile):
    pass
    

class DriverProfile(BaseProfile):
    bio = models.TextField(null=True, blank=True)
    mc_dot_number = models.CharField(max_length=10, null=True, blank=True)
    car = models.ForeignKey(CarInfo, on_delete=models.CASCADE, related_name="driver_car", null=True, blank=True)
    status = models.CharField(max_length=55, choices=DRIVER_STATUS, blank=True)
    
    
class CompanyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company_profile")
    company_name = models.CharField(max_length=155, null=True, blank=True)
    registration_number = models.CharField(max_length=30, null=True, blank=True)
    company_license = models.TextField(null=True, blank=True)
    company_license_file = models.FileField(upload_to=f"company license/license/{company_name}/", null=True, blank=True)
    insurance_contract = models.TextField(null=True, blank=True)
    insurance_contract_file = models.FileField(upload_to=f"campany contract/contract/{company_name}/", null=True, blank=True)
    phone = PhoneNumberField(blank=True, null=True)
    billing_address = models.CharField(max_length=155, null=True, blank=True)
    mc_dot_number = models.CharField(max_length=10, null=True, blank=True)
    auto_park = models.ManyToManyField(CarInfo, related_name="company_autopark", blank=True)
    company_user = models.BooleanField(default=False, blank=True)
    link = models.CharField(max_length=155, blank=True, null=True)
    
    def create_link(self):
        import uuid
        from decouple import config
        code = str(uuid.uuid4())
        self.link = f"http://{config('SERVER_IP')}/api/v1/register/company/driver/{code}/"

    def __str__(self):
        return self.user.email
    
    
class CompanyDriverProfile(BaseProfile):
    company = models.OneToOneField(CompanyProfile, on_delete=models.CASCADE, related_name="company_driver_profile")
    bio = models.TextField(null=True, blank=True)
    car = models.ForeignKey(CarInfo, on_delete=models.CASCADE, related_name="company_driver_car", null=True, blank=True)
    mc_dot_number = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=55, choices=DRIVER_STATUS, blank=True)