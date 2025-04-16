from django.db import models
from django.conf import settings


class MootCourtType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Тип муткорта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип муткорта"
        verbose_name_plural = "Типы муткортов"


class MootCourtTag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Тег")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег муткорта"
        verbose_name_plural = "Теги муткортов"


class Event(models.Model):
    start_time = models.DateTimeField(verbose_name="Дата и время начала")
    end_time = models.DateTimeField(null=True, blank=True, verbose_name="Дата и время окончания")
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    files = models.ManyToManyField('technical.Document', blank=True, related_name='events', verbose_name="Файлы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class MootCourtStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name="Статус муткорта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус муткорта"
        verbose_name_plural = "Статусы муткортов"


class ObjectStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name="Статус объекта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус объекта"
        verbose_name_plural = "Статусы объектов"


class MootCourt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_mootcourts')
    premoot = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='pre_moots')
    type = models.ForeignKey(MootCourtType, on_delete=models.PROTECT, related_name='mootcourts')
    tags = models.ManyToManyField(MootCourtTag, blank=True, related_name='mootcourts')
    announcement = models.TextField(verbose_name="Анонс")
    messages = models.ManyToManyField('technical.Message', blank=True, related_name='mootcourts')
    events = models.ManyToManyField(Event, related_name='mootcourts')
    documents = models.ManyToManyField('technical.Document', related_name='mootcourts')
    require_telegram = models.BooleanField(default=False, verbose_name="Необходимость Telegram-канала")
    telegram_channel = models.CharField(max_length=255, blank=True, null=True)
    teams = models.ManyToManyField('users.Team', blank=True, related_name='mootcourts')
    senior_arbitrators = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='senior_arbitrator_mootcourts')
    arbitrators = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='arbitrator_mootcourts')
    status = models.ForeignKey(MootCourtStatus, on_delete=models.PROTECT, related_name='mootcourts')
    background = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='mootcourt_images/', blank=True, null=True)
    object_status = models.ForeignKey(ObjectStatus, on_delete=models.PROTECT, related_name='mootcourts')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Муткорт"
        verbose_name_plural = "Муткорты"


class MootCourtImage(models.Model):
    mootcourt = models.ForeignKey(
        'MootCourt',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="Муткорт"
    )
    image = models.ImageField(upload_to='mootcourt_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Изображение для {self.mootcourt.name}"