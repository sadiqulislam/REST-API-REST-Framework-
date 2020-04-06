from django.shortcuts import render
from .serializers import InfoSerializer, UserSerializer
from .models import Info
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, filters
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView


# Create your views here.

class InfoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Info.objects.all().order_by('-created')
    serializer_class = InfoSerializer


class UserViewSet(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class DueTaskViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all().order_by('-created').filter(completed=False)
    serializer_class = InfoSerializer


class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all().order_by('-created').filter(completed=True)
    serializer_class = InfoSerializer
