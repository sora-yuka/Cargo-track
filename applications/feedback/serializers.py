from rest_framework import serializers

from applications.feedback.models import CRating, DRating 
   
        
class CRatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='onwer.usarname')
    rating = serializers.IntegerField(min_value=1, max_value=10)
    
    class Meta:
        model = CRating
        fields = ['owner', 'rating']
        
        
class DRatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='onwer.usarname')
    rating = serializers.IntegerField(min_value=1, max_value=10)
    
    class Meta:
        model = DRating
        fields = ['owner', 'rating']