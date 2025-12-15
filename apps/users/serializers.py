from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.transaction import atomic
from.models import ProfileModel

UserModel = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    @atomic()
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        return user