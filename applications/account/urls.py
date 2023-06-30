from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from applications.account.views import (
    UserRegisterAPIView, UserActivationAPIView, PasswordChangeAPIView, 
    ForgotPasswordAPIView, ForgotPasswordConfirmAPIView
)

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view()),
    path("confirm/<uuid:activation_code>/", UserActivationAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("change_password/", PasswordChangeAPIView.as_view()),
    path("forgot_password/", ForgotPasswordAPIView.as_view()),
    path("recovery/confirm/", ForgotPasswordConfirmAPIView.as_view()),
]