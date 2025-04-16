from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema

from .models import MootCourt
from .serializers import (
    MootCourtSerializer,
    EventSerializer,
    DocumentSerializer,
    MessageSerializer,
)


class MootCourtViewSet(viewsets.ModelViewSet):
    queryset = MootCourt.objects.all().prefetch_related(
        'teams',
        'arbitrators',
        'senior_arbitrators',
        'events',
        'documents',
        'message',
        'tags'
    ).select_related(
        'organizer',
        'premoot',
        'type',
        'status',
        'object_status',
        'telegram_channel'
    )
    serializer_class = MootCourtSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    @extend_schema(summary="Список муткортов")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Создать муткорт")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Получить муткорт")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Обновить муткорт")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="Частично обновить муткорт")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="Удалить муткорт")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
