from rest_framework import serializers
from models import Bucketlist, Bucketlistitem


class BucketlistitemSerializer(serializers.ModelSerializer):
    """Define bucektlistitems serializer fields."""

    class Meta:
        model = Bucketlistitem
        fields = ('name', 'done', 'bucketlist')

        read_only_fields = ('created_at', 'updated_at')


class BucketlistSerializer(serializers.ModelSerializer):
    """Define bucketlist fields that will be serialized."""

    items = BucketlistitemSerializer()

    class Meta:
        model = Bucketlist
        fields = ('name', 'creator', 'items')

        read_only_fields = ('created_at', 'updated_at')
