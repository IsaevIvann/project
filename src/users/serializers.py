from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from src.users.models import UserPhoto

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    vuz_name = serializers.CharField(required=True)
    photo = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password',
            'first_name', 'last_name',
            'phone_number', 'post', 'description',
            'vuz_name', 'organization_link',
            'photo',
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def to_representation(self, instance):
        tokens = RefreshToken.for_user(instance)
        return {
            'refresh': str(tokens),
            'access': str(tokens.access_token),
        }


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Неверный email или пароль")
        if not user.is_active:
            raise serializers.ValidationError("Аккаунт не активен")

        tokens = RefreshToken.for_user(user)
        return {
            'refresh': str(tokens),
            'access': str(tokens.access_token),
        }


class UserPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoto
        fields = ['id', 'image', 'uploaded_at']


class UserProfileSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    photo_url = serializers.SerializerMethodField(read_only=True)
    photos = UserPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email',
            'first_name', 'last_name',
            'phone_number', 'post', 'description',
            'vuz_name', 'organization_link',
            'photo', 'photo_url', 'photos',
        ]

    def get_photo_url(self, obj) -> str:
        request = self.context.get('request')
        if obj.photo and hasattr(obj.photo, 'url'):
            return request.build_absolute_uri(obj.photo.url) if request else obj.photo.url
        return None


class UploadUserPhotoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = UserPhoto
        fields = ['image']

    def create(self, validated_data):
        user = self.context['request'].user
        return UserPhoto.objects.create(user=user, **validated_data)


class UploadUserPhotosSerializer(serializers.Serializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        allow_empty=False
    )

    def create(self, validated_data):
        user = self.context['request'].user
        images = validated_data['images']
        for image in images:
            UserPhoto.objects.create(user=user, image=image)
        return {"uploaded": len(images)}