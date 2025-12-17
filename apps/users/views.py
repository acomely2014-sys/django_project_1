from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.serializers import UserSerializer


# Create your views here.
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer


class MeView(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)