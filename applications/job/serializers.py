from rest_framework import serializers

from applications.job.models import Job
from applications.job.send_mail import send_confirmation_email, send_email_to_owner


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

        email_shipper = instance.owner.email
        email_carrier = self.context['request'].user.email
        # print(email_shipper, email_carrier)
        send_email_to_owner.delay(email_shipper, email_carrier)
        send_confirmation_email.delay(email_carrier, instance.activation_code)
        print(validated_data)
        
        return instance
