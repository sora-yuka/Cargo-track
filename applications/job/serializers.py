from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

from applications.job.models import Job
from applications.job.tasks import send_confirmation_email, send_email_to_owner
from applications.profiles.models import BaseProfile, DriverProfile


class JobSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Job
        fields = '__all__'
        
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        exclude_fields = ['activation_code', 'complete_code', 'cancel_code']
        for field in exclude_fields:
            rep.pop(field, None)
        return rep
        
        
class JobOfferSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    
    class Meta:
        model = Job
        fields = '__all__'
      
        
    def update(self, instance, validated_data):
        if instance.status == 'Loading goods':
            raise serializers.ValidationError('Sorry, but this job was taken by someone!')

        email_shipper = instance.owner.email
        email_carrier = self.context['request'].user.email
        carrier_id = self.context['request'].user.id
        # send_email_to_owner.delay(email_shipper, email_carrier)
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
        return rep

