from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import redirect
from django.utils.html import format_html
from django.conf import settings


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        verbose_name="Телефон"
    )
    photo = models.ImageField(
        upload_to='photos/',
        blank=True,
        verbose_name="Фотография"
    )
    post = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Должность"
    )
    description = models.TextField(
        max_length=2000,
        blank=True,
        verbose_name="Описание"
    )
    vuz_name = models.CharField(
        max_length=255,
        verbose_name="Название ВУЗа/организации"
    )
    organization_link = models.URLField(
        max_length=500,
        blank=True,
        verbose_name="Ссылка на ВУЗ/организацию"
    )
    accept_invite = models.BooleanField(
        default=False,
        verbose_name="Принимать приглашения в команду"
    )
    verified_user = models.BooleanField(
        default=False,
        verbose_name="Верифицированный пользователь"
    )
    rating = models.FloatField(
        default=0.0,
        verbose_name="Рейтинг"
    )

    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Активный'),
        (STATUS_INACTIVE, 'Неактивный'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
        verbose_name="Статус"
    )

    ROLE_CHOICES = [
        ('participant', 'Участник'),
        ('trainer', 'Тренер'),
        ('arbiter', 'Арбитр'),
        ('organization', 'ВУЗ/Организация'),
        ('admin', 'Администратор'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='participant',
        verbose_name='Роль пользователя'
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def change_status_button(self, obj):
        if obj.status == self.STATUS_ACTIVE:
            return format_html(
                '<a class="button" href="{}">Деактивировать</a>',
                f'../{obj.id}/deactivate/'
            )
        return format_html(
            '<a class="button" href="{}">Активировать</a>',
            f'../{obj.id}/activate/'
        )

    change_status_button.short_description = 'Изменить статус'
    change_status_button.allow_tags = True

    def activate_user(self, request, user_id):
        User.objects.filter(pk=user_id).update(status=self.STATUS_ACTIVE)
        self.message_user(request, 'Пользователь активирован.')
        return redirect('..')

    def deactivate_user(self, request, user_id):
        User.objects.filter(pk=user_id).update(status=self.STATUS_INACTIVE)
        self.message_user(request, 'Пользователь деактивирован.')
        return redirect('..')


class Team(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Название"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )

    organization = models.CharField(
        max_length=255,
        blank=False,
        default='-',
        verbose_name="ВУЗ/организация"
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name="Подтверждена ВУЗом/организацией"
    )
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name="owned_teams",
        verbose_name="Владелец"
    )
    captain = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        related_name="captained_teams",
        null=True,
        blank=True,
        verbose_name="Капитан"
    )
    coach = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        related_name="coached_teams",
        null=True,
        blank=True,
        verbose_name="Тренер"
    )
    members = models.ManyToManyField(
        'users.User',
        related_name="teams",
        verbose_name="Члены команды",
        blank=True
    )
    rating = models.IntegerField(
        default=0,
        verbose_name="Рейтинг"
    )
    status = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Статус"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"



class UserPhoto(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    image = models.ImageField(upload_to='user_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Фото пользователя {self.user.username}"
