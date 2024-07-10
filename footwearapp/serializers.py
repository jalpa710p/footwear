from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        models = Register
        fields = ['username', 'email', 'phone_no', 'password', 'confirm_password']

