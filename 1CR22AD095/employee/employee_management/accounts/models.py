# # from django.db import models


# # from django.contrib.auth.models import AbstractUser

# # class CustomUser(AbstractUser):
# #     pass
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from accounts.models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2']

# class CustomAuthenticationForm(AuthenticationForm):
#     pass
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields if needed, for example:
    email = models.EmailField(unique=True)
