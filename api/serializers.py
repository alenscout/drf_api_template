from rest_framework import serializers
from base.models import ModelOneForTest as MOFT,ModelTwoForTest as MTFT

class ModelOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = MOFT
        fields = '__all__'

class ModelTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MTFT
        fields = '__all__'
        