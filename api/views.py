from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import UserProfile
from api.serializers import UserProfileSerializers, CreateUserProfileSerializers


@api_view(["GET", "POST"])
def ListProfile(request):
    if request.method == "GET":
        data = UserProfile.objects.all()
        data_serializers = UserProfileSerializers(data, many=True)
        return Response(data_serializers.data)
    if request.method == "POST":
        req_data = request.data
        data_serializers = CreateUserProfileSerializers(data=req_data)
        data_serializers.is_valid(raise_exception=True)
        data_serializers.save()
        return Response(data_serializers.data, status=201)


@api_view(["PUT", "DELETE"])
def update_and_delete_UserProfile(request, id):
    if request.method == "PUT":
        user_get_id = UserProfile.objects.get(id=id)
        data_serializers = UserProfileSerializers(data=user_get_id)
        data_serializers.is_valid(raise_exception=True)
        data_serializers.save()
        return Response(data_serializers.data, status.HTTP_200_OK)
 