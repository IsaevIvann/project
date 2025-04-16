from rest_framework import serializers
from .models import (
    MootCourt, MootCourtType, MootCourtTag, Event,
    MootCourtStatus, ObjectStatus, MootCourtImage
)
from src.technical.models import Message, Document
from src.users.models import Team, User


class MootCourtTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MootCourtType
        fields = '__all__'


class MootCourtTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MootCourtTag
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class MootCourtStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MootCourtStatus
        fields = '__all__'


class ObjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectStatus
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'post', 'photo']


class MootCourtImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MootCourtImage
        fields = ['id', 'image', 'uploaded_at']


class MootCourtSerializer(serializers.ModelSerializer):
    type = MootCourtTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=MootCourtType.objects.all(), source='type', write_only=True
    )
    tags = MootCourtTagSerializer(many=True, read_only=True)
    tags_ids = serializers.PrimaryKeyRelatedField(
        queryset=MootCourtTag.objects.all(), many=True, write_only=True, source='tags'
    )
    events = EventSerializer(many=True, read_only=True)
    events_ids = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(), many=True, write_only=True, source='events'
    )
    messages = MessageSerializer(many=True, read_only=True)
    messages_ids = serializers.PrimaryKeyRelatedField(
        queryset=Message.objects.all(), many=True, write_only=True, source='messages'
    )
    documents = DocumentSerializer(many=True, read_only=True)
    documents_ids = serializers.PrimaryKeyRelatedField(
        queryset=Document.objects.all(), many=True, write_only=True, source='documents'
    )
    status = MootCourtStatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=MootCourtStatus.objects.all(), source='status', write_only=True
    )
    object_status = ObjectStatusSerializer(read_only=True)
    object_status_id = serializers.PrimaryKeyRelatedField(
        queryset=ObjectStatus.objects.all(), source='object_status', write_only=True
    )
    organizer = UserSerializer(read_only=True)
    organizer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='organizer', write_only=True
    )
    premoot = serializers.PrimaryKeyRelatedField(queryset=MootCourt.objects.all(), required=False, allow_null=True)
    teams = TeamSerializer(many=True, read_only=True)
    teams_ids = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), many=True, write_only=True, source='teams'
    )
    senior_arbitrators = UserSerializer(many=True, read_only=True)
    senior_arbitrators_ids = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, write_only=True, source='senior_arbitrators'
    )
    arbitrators = UserSerializer(many=True, read_only=True)
    arbitrators_ids = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, write_only=True, source='arbitrators'
    )

    images = MootCourtImageSerializer(many=True, read_only=True)
    image_files = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    class Meta:
        model = MootCourt
        fields = '__all__'

    def create(self, validated_data):
        image_files = validated_data.pop('image_files', [])
        mootcourt = super().create(validated_data)
        for image in image_files:
            MootCourtImage.objects.create(mootcourt=mootcourt, image=image)
        return mootcourt

    def update(self, instance, validated_data):
        image_files = validated_data.pop('image_files', [])
        instance = super().update(instance, validated_data)
        for image in image_files:
            MootCourtImage.objects.create(mootcourt=instance, image=image)
        return instance
