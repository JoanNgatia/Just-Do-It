"""This file defines api serializer methods to represent bucketlist details."""

from rest_framework import serializers
from bucketlist.models import Bucketlist, Bucketlistitem


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

        read_only_fields = ('created_at', 'updated_at', 'items')
