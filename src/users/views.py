from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .serializers import RegisterSerializer, LoginSerializer, UserProfileSerializer


@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = serializer.to_representation(user)
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class GetProfileView(APIView):
    def get(self, request):
        user = request.user
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': user.phone_number,
            'post': user.post,
            'description': user.description,
            'vuz_name': user.vuz_name,
            'organization_link': user.organization_link,
            'photo': request.build_absolute_uri(user.photo.url) if user.photo else None,
            'rating': user.rating,
            'status': user.status,
        }
        return Response(data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class UpdateProfileView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def patch(self, request):
        user = request.user
        for field, value in request.data.items():
            if hasattr(user, field):
                setattr(user, field, value)
        if 'photo' in request.FILES:
            user.photo = request.FILES['photo']
        user.save()
        return Response({
            'message': 'Профиль обновлён успешно',
            'first_name': user.first_name,
            'last_name': user.last_name,
            'photo': request.build_absolute_uri(user.photo.url) if user.photo else None,
        }, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class DeleteProfileView(APIView):
    def delete(self, request):
        request.user.delete()
        return Response({'message': 'Пользователь успешно удалён'}, status=status.HTTP_204_NO_CONTENT)
