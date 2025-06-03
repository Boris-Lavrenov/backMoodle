from rest_framework import viewsets
from myapi.models import User
from myapi.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #test
