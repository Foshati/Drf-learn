from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import UserProfile
from api.serializers import UserProfileSerializers


@api_view(["GET"])
def ListProfile(request):
    data = UserProfile.objects.all()
    data_serializers = UserProfileSerializers(data, many=True)
    return Response(data_serializers.data)
