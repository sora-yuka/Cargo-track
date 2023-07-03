from django.db import models

# Create your models here.


class CarType(models.Model):
    car_type = models.CharField(max_length=255)
    

class CarBrand(models.Model):
    brand = models.CharField(max_length=155)
    
    
class CarDocument(models.Model):
    document = models.TextField()
    documents_file = models.FileField(upload_to="car/documents/", null=True, blank=True)
    
    
class CarEquipment(models.Model):
    equipment = models.CharField(max_length=155)
    

class CarInfo(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name="car_brand")
    year_of_manufacture = models.PositiveIntegerField()
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    load_capacity = models.CharField(max_length=75)
    equipment = models.ForeignKey(CarEquipment, on_delete=models.CASCADE, related_name="car_equipment")
    documents = models.ForeignKey(CarDocument, on_delete=models.CASCADE, related_name="car_documents")
    car_image = models.ImageField(upload_to="car/images/")