from dj_rest_auth.registration.serializers import SocialLoginSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import RegionUpdateRequest

User = get_user_model()


class WCALoginSerializer(SocialLoginSerializer):
    access_token = None
    id_token = None


class RegionSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()


class ZoneSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "wca_id",
            "region",
            "region_updated_at",
            "created_at",
        )


class UserRegionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("region",)


class RegionUpdateRequestSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = RegionUpdateRequest
        fields = ("region", "status", "created_at")
        read_only_fields = ("status", "created_at")

    def get_status(self, obj):
        return obj.get_status_display()


class NewsSerializer(serializers.Serializer):
    from_name = serializers.CharField()
    message = serializers.CharField()
    image = serializers.URLField()
    permalink = serializers.URLField()
    created_at = serializers.DateTimeField()
