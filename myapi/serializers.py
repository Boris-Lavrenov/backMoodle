from rest_framework import  serializers
from myapi.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        #dwwd
        #Boris
