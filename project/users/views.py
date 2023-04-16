# from rest_framework import status
# from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView#, GenericAPIView, DestroyAPIView
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response

from users.serializers import UserSerializer#, UserLoginSerializer, TokenSerializer


# Create your views here.


class UserManageView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    http_method_names = ["get", "patch"]

    def get_object(self):
        return self.request.user


# class UserLoginAPIView(GenericAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UserLoginSerializer
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#
#         if not serializer.is_valid():
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         token, _ = Token.objects.get_or_create(user=serializer.user)
#         return Response(data=TokenSerializer(token).data, status=status.HTTP_200_OK)
#
#
# class UserLogoutAPIView(DestroyAPIView):
#     def get_object(self):
#         return self.request.auth
