from rest_framework import serializers
from django.contrib.auth.models import User
# ye class validate karta h 
class UserSerializer(serializers.ModelSerializer):
    # meta class batata h ki kaun sa 
    # model aur kaun sa field use karna h
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

# create new user function

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user