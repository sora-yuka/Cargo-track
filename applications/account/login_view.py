from django.utils.module_loading import import_string
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
from rest_framework_simplejwt.settings import api_settings
from applications.profiles.models import BaseProfile
from applications.account.serializers import UserRegisterSerializer
from applications.profiles.serializers import BaseSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class TokenViewBase(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = None
    _serializer_class = ""

    www_authenticate_realm = "api"

    def get_serializer_class(self):
        """
        If serializer_class is set, use it directly. Otherwise get the class from settings.
        """

        if self.serializer_class:
            return self.serializer_class
        try:
            return import_string(self._serializer_class)
        except ImportError:
            msg = "Could not import serializer '%s'" % self._serializer_class
            raise ImportError(msg)

    def get_authenticate_header(self, request):
        return '{} realm="{}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm,
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        email = request.data.get("email")
        profile_id = UserRegisterSerializer(User.objects.get(email=email)).data.get("id")
        true_key = []
        for key, value in BaseSerializer(BaseProfile.objects.get(user=profile_id)).data.items():
            if value is True:
                true_key.append(key)
        return Response(
            {   
                "token": serializer.validated_data,
                "profile": true_key
            },
            status=status.HTTP_200_OK
        )


class TokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    _serializer_class = api_settings.TOKEN_OBTAIN_SERIALIZER


token_obtain_pair = TokenObtainPairView.as_view()