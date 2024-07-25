from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import UserProfile
from api.serializers import CreateUserProfileSerializers, UserProfileSerializers


class UserProfileView(APIView):
    def post(self, request):
        serializer = CreateUserProfileSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, id=None):
        if id:
            user_profile = get_object_or_404(UserProfile, id=id)
            serializer = UserProfileSerializers(user_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            user_profiles = UserProfile.objects.all()
            serializer = UserProfileSerializers(user_profiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        user_profile = get_object_or_404(UserProfile, id=id)
        serializer = CreateUserProfileSerializers(
            instance=user_profile, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        user_profile = get_object_or_404(UserProfile, id=id)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
