""" URL Configuration for the app module """

from django.urls import path
from .views import SignupView, LoginView, VerifyEmailView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("verify-email/", VerifyEmailView.as_view(), name="verify_email"),
]
