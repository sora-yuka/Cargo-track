from rest_framework import serializers

from applications.feedback.models import Rating 
   
        
class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='onwer.usarname')
    rating = serializers.IntegerField(min_value=1, max_value=10)
    
    class Meta:
        model = Rating
        fields = ['owner', 'rating']