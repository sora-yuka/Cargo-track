from rest_framework import serializers
from applications.profiles.models import (
    BaseProfile, ShipperProfile, DriverProfile, CompanyDriver, CompanyProfile
)


class BaseSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = BaseProfile
        fields = "__all__"
        
    def validate(self, attrs):
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