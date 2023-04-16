# from django.contrib.auth import authenticate
# from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
# from rest_framework.authtoken.models import Token

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    subscriptions = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    available_subscriptions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "subscriptions", "available_subscriptions",)
        read_only_fields = ("id", "username", "available_subscriptions",)

    def get_available_subscriptions(self, instance: User):
        all_user_ids = set(User.objects.all().values_list('pk', flat=True))
        subscribed_user_ids = set(instance.subscriptions.all().values_list('pk', flat=True))
        return all_user_ids - subscribed_user_ids


# class UserLoginSerializerizer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)
#
#     default_error_messages = {
#         'inactive_account': _('User account is disabled.'),
#         'invalid_credentials': _('Unable to login with provided credentials.')
#     }
#
#     def __init__(self, *args, **kwargs):
#         super(UserLoginSerializer, self).__init__(*args, **kwargs)
#         self.user = None
#
#     def validate(self, attrs):
#         self.user = authenticate(username=attrs.get("username"), password=attrs.get('password'))
#         if not self.user:
#             raise serializers.ValidationError(self.error_messages['invalid_credentials'])
#
#         if not self.user.is_active:
#             raise serializers.ValidationError(self.error_messages['inactive_account'])
#
#         return attrs
#
#
# class TokenSerializer(serializers.ModelSerializer):
#     auth_token = serializers.CharField(source='key')
#
#     class Meta:
#         model = Token
#         fields = ("auth_token", "created")
