"""This file defines api serializer methods to represent account/user info."""
from rest_framework import serializers
from bucketlist.models import Account


class AccountSerializer(serializers.ModelSerializer):
    """Define User serialization fields."""

    class Meta:
        """Define metadata the serializer should use."""

        model = Account
        fields = ('username', 'password', 'tagline')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, **validated_data):
        """Override create method and set password."""
        user = Account(
            username=validated_data['username'],
            tagline=validated_data['tagline']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
