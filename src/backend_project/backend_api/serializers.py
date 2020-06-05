from rest_framework import serializers

from . import models


class ActivityPeriodSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.ActivityPeriod
        fields = ('start_time', 'end_time')

class ActivitySerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""
    activity_period = ActivityPeriodSerializer(read_only=True, many=True)

    class Meta:
        model = models.ActivityLog
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
