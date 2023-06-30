from datetime import datetime
from random import randint
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model
from applications.account.models import make_password, Recovery
from applications.account.tasks import send_recovery_code

User = get_user_model()


class CarrierRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=8, required=True, write_only=True)
    company = serializers.CharField(min_length=3, required=True)
    mc_dot_number = serializers.CharField(min_length=9, required=True)
    
    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "email", "password", "password_confirm",
            "phone", "company", "billing_address", "mc_dot_number",
        ]
    
    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")
        mc_dot_number = attrs.get("mc_dot_number")
        billing_address = attrs.get("billing_address")
        
        if (
                not mc_dot_number.startswith("MC#") or len(mc_dot_number) != 9
            ) and (
                not mc_dot_number.startswith("DOT#") or len(mc_dot_number) != 10
            ):
            raise serializers.ValidationError("Incorrect MC/DOT number.")
        
        if len(billing_address.split(",")) != 3:
            raise serializers.ValidationError("Incoreect billing address")
        
        if password != password_confirm:
            raise serializers.ValidationError("Password are not similar!")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user
    
    

    
    
class RecoverySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recovery
        fields = "__all__"
    

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(min_length = 8, required = True)
    new_password = serializers.CharField(min_length = 8, required = True)
    new_password_confirm = serializers.CharField(min_length = 8, required = True)
    
    def validate(self, attrs):
        new_password = attrs.get("new_password")
        new_password_confirm = attrs.pop("new_password_confirm")

        if new_password != new_password_confirm:
            raise serializers.ValidationError("Password are not similar!")
        return attrs
    
    def validate_old_password(self, old_password):
        request = self.context.get("context")
        user = request.user
        
        if not user.check_password(old_password):
            raise serializers.ValidationError("Wrong password.")
        return old_password
    
    def set_new_password(self):
        user = self.context.get("context").user
        password = self.validated_data.get("new_password")
        user.password = make_password(password)
        user.save()
        
        
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    
    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User doesn't exists.")
        return email
    
    def send_code(self):
        email = self.validated_data.get("email")
        user = User.objects.get(email=email)
        code = randint(0000_0000, 9999_9999)
        send_recovery_code.delay(user_email=email, code=code)
        recovery = Recovery.objects.create(
            email=user, recovery_code=code, password_requested=timezone.now()
        )
        recovery.save()
        
        
class ForgotPasswordConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=8, required=True)
    password = serializers.CharField(min_length=8, required=True)
    password_confirm = serializers.CharField(min_length=8, required=True)
    
    @staticmethod 
    def validate_code(code):
        if not Recovery.objects.filter(recovery_code=code).first():
            raise serializers.ValidationError("Code entered incorrectly.")
        return code
    
    def validate(self, attrs):
        code = attrs.get("code")
        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")
            
        recovery = Recovery.objects.filter(recovery_code=code).first()
        request_time = timezone.now() - recovery.password_requested

        if request_time.total_seconds() > 24 * 60 * 60:
            raise serializers.ValidationError("The code has expired, please make a new request")
        
        if password != password_confirm:
            raise serializers.ValidationError("Password are not similar!")
        
        return attrs
    
    def set_new_password(self, email):
        user = User.objects.get(email=email)
        password = self.validated_data.get("password")
        user.password = make_password(password)
        user.save()