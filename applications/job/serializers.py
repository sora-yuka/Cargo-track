from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

from applications.job.models import Job
from applications.job.tasks import send_confirmation_email, send_email_to_owner
from applications.profiles.models import BaseProfile, DriverProfile, ShipperProfile


class JobSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Job
        fields = '__all__'
        
        
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        exclude_fields = ['activation_code', 'complete_code', 'cancel_code']
        for field in exclude_fields:
            rep.pop(field, None)
        rep['owner'] = ShipperProfile.objects.get(user_id=User.objects.get(id=instance.owner.id)).id
        return rep
        
        
class JobOfferSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    
    class Meta:
        model = Job
        fields = '__all__'
      
        
    def update(self, instance, validated_data):
        if instance.status == 'Loading goods':
            raise serializers.ValidationError('Sorry, but this job was taken by someone!')
        
        delivery_date = validated_data.get('delivary_date')
        destination_location = validated_data.get('destination_location')
        pickup_date = validated_data.get('pickup_date')
        pickup_location = validated_data.get('pickup_location')
        required_equipment = validated_data.get('required_equipment')
        title = validated_data.get('title')
        type_of_goods = validated_data.get('type_of_goods')
        weight_of_goods = validated_data.get('weight_of_goods')
        
        if delivery_date:
            instance.delivery_date = delivery_date
        if destination_location:
            instance.destination_location = destination_location
        if pickup_date:
            instance.pickup_date = pickup_date
        if pickup_location:
            instance.pickup_location = pickup_location
        if required_equipment:
            instance.required_equipment = required_equipment
        if title:
            instance.title = title
        if type_of_goods:
            instance.type_of_goods = type_of_goods
        if weight_of_goods:
            instance.weight_of_goods = weight_of_goods
            
        
        email_shipper = instance.owner.email
        email_carrier = self.context['request'].user.email
        carrier_id = self.context['request'].user.id
        send_email_to_owner.delay(email_shipper, email_carrier)
        send_confirmation_email.delay(email_carrier, instance.activation_code, instance.cancel_code, instance.id)
        
        driver_profile= DriverProfile.objects.get(user_id=User.objects.get(id=carrier_id))
        driver_profile.status = 'busy'

        instance.status = 'Loading goods'
        instance.driver_id = carrier_id
        driver_profile.save()
        instance.save()
    
        return instance
    
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        exclude_fields = ['activation_code', 'complete_code', 'cancel_code']
        for field in exclude_fields:
            rep.pop(field, None)
        rep['owner'] = ShipperProfile.objects.get(user_id=User.objects.get(id=instance.owner.id)).id
        return rep

