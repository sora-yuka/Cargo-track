from rest_framework import serializers

from applications.job.models import Job


class JobSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Job
        fields = '__all__'
        
