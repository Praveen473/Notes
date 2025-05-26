
from rest_framework import serializers
from .models import table
class tableserial(serializers.ModelSerializer):
    class Meta:
        model=table
        fields="__all__"
