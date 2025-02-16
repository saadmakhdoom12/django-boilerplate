"""Views for the app."""

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer, SignupSerializer
from .token import account_activation_token

User = get_user_model()


class SignupView(APIView):
    """signup view"""

    def post(self, request):
        """post method"""

        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(commit=False)
            if isinstance(user, User):
                user.save()
            else:
                return Response(
                    {"error": "User creation failed."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            token = account_activation_token.make_token(user)
            # Send verification email
            send_mail(
                subject="Verify your email",
                message=f"Your token is: {token}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )
            return Response(
                {
                    "message": (
                        "User created successfully. "
                        "Check your email for verification."
                    )
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            if not isinstance(validated_data, dict):
                return Response(
                    {"error": "Validation failed."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user = authenticate(
                username=validated_data.get("username"),
                password=validated_data.get("password"),
            )
            if user:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"error": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    def post(self, request):
        token = request.data.get("token")
        email = request.data.get("email")
        try:
            user = User.objects.get(email=email)
            if account_activation_token.check_token(user, token):
                user.email_verified = (
                    True  # Correct assignment to the user instance
                )
                user.save()
                return Response(
                    {"message": "Email verified successfully."},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST
            )
        except User.DoesNotExist:
            return Response(
                {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )
