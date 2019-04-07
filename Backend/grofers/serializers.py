from rest_framework import serializers
from .models import *


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('key', 'value')