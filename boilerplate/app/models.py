"""Basic imports"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """custom user"""

    email_verified = models.BooleanField(default=False)
