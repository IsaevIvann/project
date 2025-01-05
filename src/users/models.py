from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import redirect
from django.utils.html import format_html


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Телефон"
    )
    photo = models.ImageField(
        upload_to='photos/',
        blank=True,
        null=True,
        verbose_name="Фотография"
    )
    post = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Должность"
    )
    description = models.CharField(
        max_length=2000,
        blank=True,
        null=True,
        verbose_name="Должность"
    )
    vuz_name = models.CharField(
        max_length=15,
        blank=False,
        null=True,
        verbose_name="Название ВУЗа/организации"
    )
    organization_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
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
    STATUS_CHOICES = [
        ('active', 'Активный'),
        ('inactive', 'Неактивный'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name="Статус"
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def change_status_button(self, obj):
        if obj.status == 'active':
            return format_html(
                '<a class="button" href="{}">Деактивировать</a>',
                f'../{obj.id}/deactivate/'
            )
        else:
            return format_html(
                '<a class="button" href="{}">Активировать</a>',
                f'../{obj.id}/activate/'
            )
    change_status_button.short_description = 'Изменить статус'
    change_status_button.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:user_id>/activate/', self.admin_site.admin_view(self.activate_user), name='activate_user'),
            path('<int:user_id>/deactivate/', self.admin_site.admin_view(self.deactivate_user), name='deactivate_user'),
        ]
        return custom_urls + urls

    def activate_user(self, request, user_id):
        User.objects.filter(pk=user_id).update(status='active')
        self.message_user(request, 'Пользователь активирован.')
        return redirect('..')

    def deactivate_user(self, request, user_id):
        User.objects.filter(pk=user_id).update(status='inactive')
        self.message_user(request, 'Пользователь деактивирован.')
        return redirect('..')


class Team(models.Model):
    # date_created = models.DateTimeField(
    #     auto_now_add=True,
    #     verbose_name="Дата создания"
    # )
    date_field = models.CharField(
        max_length=15,
        blank=False,
        null=True,
        verbose_name="Дата создания"
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Название"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to="team_logos/",
        blank=True,
        null=True,
        verbose_name="Логотип"
    )
    organization = models.CharField(
        max_length=255,
        blank=True,
        null=True,
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
        max_length=100, blank=True,
        null=True, verbose_name="Статус"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"



