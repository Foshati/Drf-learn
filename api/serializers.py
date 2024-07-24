from rest_framework import serializers
from api.models import UserProfile


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class CreateUserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "name",
            "age",
            "bio",
            "email",
        )
