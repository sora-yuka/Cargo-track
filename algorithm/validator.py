""" Driver registration
class CarrierRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=8, required=True, write_only=True)
    mc_dot_number = serializers.CharField(min_length=9, required=True)
    billing_address = attrs.get("billing_address")

    def validate(self, attrs):
            password = attrs.get("password")
            password_confirm = attrs.pop("password_confirm")
            mc_dot_number = attrs.get("mc_dot_number")
            billing_address = attrs.get("billing_address")
            
            if (
                    not mc_dot_number.startswith("MC#") or len(mc_dot_number) != 9
                ) and (
                    not mc_dot_number.startswith("DOT#") or len(mc_dot_number) != 10
                ):
                raise serializers.ValidationError("Incorrect MC/DOT number.")
            
            if len(billing_address.split(",")) != 3:
                raise serializers.ValidationError("Incoreect billing address")
            
            if password != password_confirm:
                raise serializers.ValidationError("Password are not similar!")
            return attrs
"""



""" 
FUUUUUUUUUUCK

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
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE, related_name="car_type")
    load_capacity = models.CharField(max_length=75)
    equipment = models.ForeignKey(CarEquipment, on_delete=models.CASCADE, related_name="car_equipment")
    documents = models.ForeignKey(CarDocument, on_delete=models.CASCADE, related_name="car_documents")
    car_image = models.ImageField(upload_to="car/images/")
    
""" 