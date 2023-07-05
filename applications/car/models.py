from django.db import models

CAR_TYPE = (
    ("Euro-Track", "Euro-Track"),
    ("Container", "Container"),
    ("Tank", "Tank"),
    ("Refrigerator", "Refrigerator"),
)


class CarInfo(models.Model):
    brand = models.CharField(max_length=75)
    year_of_manufacture = models.PositiveIntegerField()
    car_type = models.CharField(max_length=55, choices=CAR_TYPE)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    load_capacity = models.CharField(max_length=75)
    equipment = models.TextField(null=True, blank=True)
    documents = models.TextField()
    documents_file = models.FileField(upload_to=f"car/{brand}/document", null=True, blank=True)
    car_image = models.ImageField(upload_to="car/images/")
    
    def __str__(self):
        return self.brand