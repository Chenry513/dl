# main/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserPreference, ModelInfo

class ModelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelInfo
        fields = '__all__'

class UserPreferenceCreateSerializer(serializers.ModelSerializer):
    model_id = serializers.PrimaryKeyRelatedField(queryset=ModelInfo.objects.all(), source='model')

    class Meta:
        model = UserPreference
        fields = ['model_id', 'preference']

class UserPreferenceSerializer(serializers.ModelSerializer):
    model = ModelInfoSerializer()

    class Meta:
        model = UserPreference
        fields = ['id', 'model', 'preference'] 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    preferences = UserPreferenceSerializer(many=True, read_only=True, source='userpreference_set')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'preferences']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user