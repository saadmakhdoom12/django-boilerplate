"""imports"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail
from django.conf import settings
from .serializers import SignupSerializer
from django.contrib.auth import get_user_model
from boilerplate.app.token import account_activation_token

User = get_user_model()


class SignupView(APIView):
    """signup view"""

    def post(self, request):
        """post method"""

        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
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
