""" Driver registration
class CarrierRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=8, required=True, write_only=True)
    mc_dot_number = serializers.CharField(min_length=9, required=True)
    billing_address = attrs.get("billing_address")

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
"""