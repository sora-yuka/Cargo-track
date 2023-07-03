from rest_framework import serializers

from applications.job.models import Job
from applications.job.tasks import send_confirmation_email, send_email_to_owner


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
        if instance.status == 'Delivering':
            raise serializers.ValidationError('Sorry, but this job was taken by someone!')

        email_shipper = instance.owner.email
        email_carrier = self.context['request'].user.email
        carrier_id = self.context['request'].user.id
        send_email_to_owner.delay(email_shipper, email_carrier)
        send_confirmation_email.delay(email_carrier, instance.activation_code, instance.cancel_code, instance.id)
        
        instance.status = 'Loading goods'
        instance.driver_id = carrier_id
        instance.save()
    
        return instance
    
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        exclude_fields = ['activation_code', 'complete_code', 'cancel_code']
        for field in exclude_fields:
            rep.pop(field, None)
        return rep

