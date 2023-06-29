from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from applications.account.serializers import UserRegisterSerializer
from applications.account.tasks import send_activation_code

User = get_user_model()


class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        try:
            serializer = UserRegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
        except IntegrityError:
            return Response(
                {
                    "message": "Something get wrong, please, check the input",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )
        
        if user:
            send_activation_code.delay(user.email, user.activation_code)
            return Response(
                "Registered successfully, we've sent verification code to your email.",
                status = status.HTTP_201_CREATED
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class UserActivationAPIView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ""
            user.save()
            return Response(
                {
                    "message": "You've successfully activated your account.",
                    "status": status.HTTP_200_OK,
                }
            )
        except User.DoesNotExist:
            return Response(
                {
                    "message": "User doesn't exists.",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )