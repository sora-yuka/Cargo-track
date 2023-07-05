from rest_framework import serializers
from applications.profiles.models import (
    BaseProfile, ShipperProfile, DriverProfile, CompanyDriverProfile, CompanyProfile
)
from django.db.models import Avg


class BaseSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = BaseProfile
        fields = [
            "id", "user", "username", "first_name", "last_name",
            "phone", "billing_address", "image", 
            "shipper" ,"driver" ,"company_driver",
        ]
        
        
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return rep

        
class ShipperSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = ShipperProfile
        # fields = "__all__"
        exclude = ["shipper", "driver", "company_driver"]
    

    def update(self, instance, validated_data):
        username = validated_data.get("username")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        phone = validated_data.get("phone")
        image = validated_data.get("image")
        billing_address = validated_data.get("billing_address")
        
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
        
        if billing_address:
            if len(billing_address.split(",")) != 3:
                raise serializers.ValidationError("Incoreect billing address")
            instance.billing_address = billing_address
        
        instance.save()
        return instance


class DriverSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = DriverProfile
        fields = "__all__"
        
    def update(self, instance, validated_data):
        username = validated_data.get("username")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        phone = validated_data.get("phone")
        image = validated_data.get("image")
        billing_address = validated_data.get("billing_address")
        bio = validated_data.get("bio")
        mc_dot_number = validated_data.get("mc_dot_number")
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
    
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return rep
    

class ShipperSerializer(BaseSerializer):
    
    class Meta:
        model = ShipperProfile
        fields = "__all__"
        
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     exclude_fields = ['rating']
    #     for field in exclude_fields:
    #         rep.pop(field, None)
    #     return rep


class DriverSerializer(BaseSerializer):
    
    class Meta:
        model = DriverProfile
        fields = "__all__"


    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return rep


class CompanyDriverSerializer(BaseSerializer):
    
    class Meta:
        model = CompanyDriverProfile
        fields = "__all__"
    
    
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return rep
        
    
class CompanySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = CompanyProfile
        fields = "__all__"
        
        
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return rep