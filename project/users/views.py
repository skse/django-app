from rest_framework.generics import RetrieveUpdateAPIView

from users.serializers import UserSerializer


# Create your views here.


class UserManageView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    http_method_names = ["get", "patch"]

    def get_object(self):
        return self.request.user
