from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User

from .models import ModelInfo, UserPreference
from .serializers import (
    ModelInfoSerializer,
    UserPreferenceSerializer,
    UserPreferenceCreateSerializer,
    UserSerializer
)

class ModelInfoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing ModelInfo instances.
    """
    queryset = ModelInfo.objects.all()
    serializer_class = ModelInfoSerializer


class UserProfileView(generics.RetrieveAPIView):
    """
    API view to retrieve user profile.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserRegistrationView(generics.CreateAPIView):
    """
    API view to handle user registration.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPreferenceListView(generics.RetrieveAPIView):
    """
    API view to retrieve user preferences.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        preferences = UserPreference.objects.filter(user=request.user)
        serializer = UserPreferenceSerializer(preferences, many=True)
        return Response(serializer.data)


class UserPreferenceCreateView(generics.CreateAPIView):
    """
    API view to create user preferences.
    """
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Overridden create method to handle user preference creation.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def handle_exception(self, exc):
        """
        Overridden exception handler to log validation errors.
        """
        response = super().handle_exception(exc)
        if response.status_code == 400:
            print("Validation error:", exc.detail)
        return response


class UserPreferenceUpdateView(generics.UpdateAPIView):
    """
    API view to update user preferences.
    """
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserPreference.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)