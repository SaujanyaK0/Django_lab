from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('user', 'user'),
        ('member', 'Member'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='member'
    )
def __str__(self):
    return f"{self.username} ({self.get_user_type_display()})"

