from rest_framework import serializers
from applications.profiles.models import (
    BaseProfile, ShipperProfile, DriverProfile, CompanyDriverProfile, CompanyProfile
)
from applications.feedback.serializers import CRatingSerializer, DRatingSerializer
from applications.car.serializers import CarInfoSerializer
from decouple import config
from django.db.models import Avg


class BaseSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = BaseProfile
        fields = [
            "id", "user", "username", "first_name", "last_name",
            "phone", "billing_address", "image", 
            "shipper" ,"driver" ,"company_driver"
        ]

        
class ShipperSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = ShipperProfile
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
        exclude = ["shipper", "driver", "company_driver"]
        
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
        car_info = CarInfoSerializer(instance.car).data
        car_info['car_image'] = f"http://{config('SERVER_IP')}{car_info.get('car_image')}"
        car_info['documents_file'] = f"http://{config('SERVER_IP')}{car_info.get('documents_file')}"
        rep['rating'] = instance.dratings.all().aggregate(Avg('rating'))['rating__avg']
        rep['car_info'] = car_info
        return rep
    
    
class CompanyDriverSerializer(DriverSerializer):
    
    class Meta:
        model = CompanyDriverProfile
        exclude = ["shipper", "driver", "company_driver"]
    
    
class CompanySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = CompanyProfile
        fields = "__all__"
        
    def update(self, instance, validated_data):
        company_name = validated_data.get("username")
        registration_number = validated_data.get("first_name")
        company_license = validated_data.get("last_name")
        company_license_file = validated_data.get("company_license_file")
        insurance_contract = validated_data.get("insurance_contract")
        insurance_contract_file = validated_data.get("insurance_contract_file")
        mc_dot_number = validated_data.get("mc_dot_number")
        phone = validated_data.get("phone")
        billing_address = validated_data.get("billing_address")
        auto_park = validated_data.get("auto_park")

        if company_name:
            instance.company_name = company_name

        if registration_number:
            instance.registration_number = registration_number

        if company_license:
            instance.company_license = company_license

        if company_license_file:
            instance.company_license_file = company_license_file

        if phone:
            instance.phone = phone

        if insurance_contract:
            instance.insurance_contract = insurance_contract

        if insurance_contract_file:
            instance.insurance_contract_file = insurance_contract_file

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

        if auto_park:
            instance.auto_park = auto_park

        instance.save()
        return instance
        
        
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        car_info = CarInfoSerializer(instance.auto_park, many=True).data
        rep['rating'] = instance.cratings.all().aggregate(Avg('rating'))['rating__avg']
        rep['car'] = []
        for i in range(len(car_info)):
            rep['car'].append(car_info[i].get('id'))
            rep['car'].append(car_info[i].get('brand'))
            rep['car'].append(car_info[i].get('car_type'))
            rep['car'].append(f"http://{config('SERVER_IP')}"+car_info[i].get   ('car_image'))
        return rep