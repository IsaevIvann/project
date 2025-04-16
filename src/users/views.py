from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer,
    UploadUserPhotoSerializer,
    UploadUserPhotosSerializer
)


@method_decorator(csrf_exempt, name='dispatch')
@extend_schema(
    request=RegisterSerializer,
    responses={201: OpenApiResponse(description="Пользователь успешно зарегистрирован. Возвращаются JWT токены.")},
    tags=['Auth'],
    summary="Регистрация пользователя с фото"
)
class RegisterView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = serializer.to_representation(user)
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
@extend_schema(
    request=LoginSerializer,
    responses={200: OpenApiResponse(description="JWT токены при успешной авторизации")},
    tags=['Auth'],
    summary="Авторизация пользователя"
)
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    responses={200: UserProfileSerializer},
    tags=['User'],
    summary="Получить профиль текущего пользователя"
)
class GetProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    request=UserProfileSerializer,
    responses={200: UserProfileSerializer},
    tags=['User'],
    summary="Обновить профиль пользователя"
)
class UpdateProfileView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializer = UserProfileSerializer(
            request.user,
            data=request.data,
            context={'request': request},
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    responses={204: OpenApiResponse(description="Профиль успешно удалён")},
    tags=['User'],
    summary="Удалить пользователя"
)
class DeleteProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        request.user.delete()
        return Response({'message': 'Пользователь успешно удалён'}, status=status.HTTP_204_NO_CONTENT)


@extend_schema(
    request=UploadUserPhotoSerializer,
    responses={201: UploadUserPhotoSerializer},
    tags=['User'],
    summary="Загрузить фото пользователя"
)
class UploadUserPhotoView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UploadUserPhotoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            photo = serializer.save()
            return Response({
                'message': 'Фото загружено',
                'data': UploadUserPhotoSerializer(photo, context={'request': request}).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    request=UploadUserPhotosSerializer,
    responses={201: OpenApiResponse(description="Фотографии успешно загружены")},
    tags=['User'],
    summary="Загрузить несколько фото пользователя"
)
class UploadUserPhotosView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UploadUserPhotosSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Фотографии успешно загружены"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['Auth'],
    summary='Обновление токена',
    request=TokenRefreshSerializer,
    responses={200: TokenRefreshSerializer},
)
class CustomTokenRefreshView(TokenRefreshView):
    pass