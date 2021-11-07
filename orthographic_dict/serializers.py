from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Word, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ("title", "post")


class RotatsiyaSerializer(serializers.ModelSerializer):
    word_id = serializers.IntegerField(read_only=True)
    _type = serializers.CharField(max_length=3, read_only=True)



class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', "username", 'password', 'password2', "token"]

    token = serializers.CharField(max_length=100, read_only=True)
    password = serializers.CharField(max_length=100, write_only=True)
    password2 = serializers.CharField(max_length=100, write_only=True)

    def validate(self, attrs):
        password = attrs.get('password', None)
        password2 = attrs.get('password2', None)
        if password != password2:
            raise serializers.ValidationError({'password': 'not matched'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'])
        token = Token.objects.create(user=user)
        return {
            "id": user.id,
            "username": user.username,
            "token": token.key
        }


class UserLoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    token = serializers.CharField(max_length=64, read_only=True)
    password = serializers.CharField(max_length=100, write_only=True)

    def create(self, validated_data):
        user = authenticate(**validated_data)
        if user is None:
            raise serializers.ValidationError({'detail': 'username or password incorrect'})
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)

        return {'id': user.id, 'username': user.username, 'token': token.key}