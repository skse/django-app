from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    subscriptions = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    available_subscriptions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "subscriptions",
            "available_subscriptions",
        )
        read_only_fields = (
            "id",
            "username",
            "available_subscriptions",
        )

    def get_available_subscriptions(self, instance: User):
        all_user_ids = set(User.objects.all().values_list('pk', flat=True))
        subscribed_user_ids = set(instance.subscriptions.all().values_list('pk', flat=True))
        return all_user_ids - subscribed_user_ids
