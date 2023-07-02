from rest_framework import serializers

from applications.job.models import Job
from applications.job.tasks import send_confirmation_email, send_email_to_owner


class JobSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Job
        fields = '__all__'
        

class JobOfferSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    
    class Meta:
        model = Job
        fields = '__all__'
        
    def update(self, instance, validated_data):
        if instance.status == 'Delivering':
            raise serializers.ValidationError('Sorry, but this job is taken by someone!')

        email_shipper = instance.owner.email
        email_carrier = self.context['request'].user.email
        # send_email_to_owner.delay(email_shipper, email_carrier)
        send_confirmation_email.delay(email_carrier, instance.activation_code, instance.cancel_code, instance.id)
        instance.status = 'Negotiations are underway'
        instance.save()
    
        return instance
