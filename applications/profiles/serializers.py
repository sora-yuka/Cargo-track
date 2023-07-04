from rest_framework import serializers
from applications.profiles.models import (
    BaseProfile, ShipperProfile, DriverProfile, CompanyDriver, CompanyProfile
)


class BaseSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = BaseProfile
        fields = "__all__"
        
    def update(self, instance, validated_data):
        username = validated_data.get("username")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        phone = validated_data.get("phone")
        image = validated_data.get("image")
        bio = validated_data.get("bio")
        mc_dot_number = validated_data.get("mc_dot_number")
        billing_address = validated_data.get("billing_address")
        car = validated_data.get("car")
        
        if username:
            instance.username = username
        
        if first_name:
            instance.first_name = first_name

        if last_name:
            instance.last_name = last_name
        
        if phone:
            instance.phone = phone
        
        if image:
            instance.image = image
            
        if bio:
            instance.bio = bio
            
        if mc_dot_number:
            if (
                    not mc_dot_number.startswith("MC#") or len(mc_dot_number) != 9
                ) and (
                    not mc_dot_number.startswith("DOT#") or len(mc_dot_number) != 10
                ):
                raise serializers.ValidationError("Incorrect MC/DOT number.")
            instance.mc_dot_number = mc_dot_number
        
        if billing_address:
            if len(billing_address.split(",")) != 3:
                raise serializers.ValidationError("Incoreect billing address")
            instance.billing_address = billing_address
        
        if car:
            instance.car = car
        
        instance.save()
        return instance
    

class ShipperSerializer(BaseSerializer):
    
    class Meta:
        model = ShipperProfile
        fields = "__all__"


class DriverSerializer(BaseSerializer):
    
    class Meta:
        model = DriverProfile
        fields = "__all__"
        

class CompanyDriverSerializer(BaseSerializer):
    
    class Meta:
        model = CompanyDriver
        fields = "__all__"
        
    
class CompanySerializer(BaseSerializer):
    
    class Meta:
        model = CompanyProfile
        fields = "__all__"