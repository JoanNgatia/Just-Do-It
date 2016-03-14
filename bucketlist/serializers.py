from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers
from models import Account, Bucketlist, Bucketlistitem


class AccountSerializer(serializers.ModelSerializer):
    """Define User serialization fields."""

    # define that password can be changed only if need be
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    bucketlists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Bucketlist.objects.all())

    class Meta:
        """Define metadata the serializer should use."""

        model = Account
        fields = ('id', 'username', 'created_at', 'updated_at',
                  'tagline', 'password', 'confirm_password', 'bucketlists')
        read_only_fields = ('created_at', 'updated_at',)

    def create(self, **validated_data):
        """Deserialize json and create a new user."""
        return Account.objects.create(validated_data)

    def update(self, instance, **validated_data):
        """Deserialize json and update user details."""
        instance.tagline = validated_data.get('tagline', instance.tagline)

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        # incase of password update check that both fields have been filled
        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()
        # save updated password to current session to avoid re-logging in
        update_session_auth_hash(self.context.get('request'), instance)

        return instance


class BucketlistitemSerializer(serializers.ModelSerializer):
    """Define bucketlistitems serializer fields."""

    class Meta:
        model = Bucketlistitem
        fields = ('id', 'name', 'done', 'bucketlist',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class BucketlistSerializer(serializers.ModelSerializer):
    """Define bucketlist fields that will be serialized."""

    creator = serializers.ReadOnlyField(source='creator.username')
    items = BucketlistitemSerializer(many=True, read_only=True)

    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'creator', 'created_at', 'updated_at', 'items')

        read_only_fields = ('id', 'created_at', 'updated_at', 'items')
