from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=8, required=True, write_only=True)
    
    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "email", "password", "password_confirm", 
            "company", "billing_address", "mc_dot_number",
        ]
    
    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")
        
        if password != password_confirm:
            raise serializers.ValidationError("Password are not similar!")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user
    
