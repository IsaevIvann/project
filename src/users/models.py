from django.contrib.auth.models import AbstractUser
from django.db import models



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
        max_length = 500,
        blank = True,
        null = True,
        verbose_name = "Ссылка на ВУЗ/организацию"
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

# class Team(models.Model):
#     date_field = models.CharField(
#         max_length=15,
#         blank=True,
#         null=True,
#         verbose_name="Дата создания"
#     )
#     name = models.CharField(
#         max_length=255,
#         unique=True,
#         verbose_name="Название"
#     )
#     description = models.TextField(
#         blank=True,
#         null=True,
#         verbose_name="Описание"
#     )
#     logo = models.ImageField(
#         upload_to="team_logos/",
#         blank=True,
#         null=True,
#         verbose_name="Логотип"
#     )
#     organization = models.CharField(
#         max_length=255,
#         blank=True, null=True,
#         verbose_name="ВУЗ/организация"
#     )
#     is_verified = models.BooleanField(
#         default=False,
#         verbose_name="Подтверждена ВУЗом/организацией"
#     )
#     owner = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="owned_teams",
#         verbose_name="Владелец"
#     )
#     captain = models.ForeignKey(
#         User,
#         on_delete=models.SET_NULL,
#         related_name="captained_teams",
#         null=True,
#         blank=True,
#         verbose_name="Капитан"
#     )
#     coach = models.ForeignKey(
#         User,
#         on_delete=models.SET_NULL,
#         related_name="coached_teams",
#         null=True,
#         blank=True,
#         verbose_name="Тренер"
#     )
#     members = models.ManyToManyField(
#         User,
#         related_name="teams",
#         verbose_name="Члены команды",
#         blank=True
#     )
#     rating = models.IntegerField(
#         default=0,
#         verbose_name="Рейтинг"
#     )
#     status = models.CharField(
#         max_length=100, blank=True,
#         null=True, verbose_name="Статус"
#     )
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Команда"
#         verbose_name_plural = "Команды"




# Дата создания  - Дата-время +  +
# Имя - Строка +  +
# Email - Строка  +  +
# Телефон - число +
# Должность - Строка    _+
# Фото - Файл      +
# Описание - Строка     +
# Название ВУЗа/организации - Строка +
# Ссылка с названия ВУЗа/организации - Ссылка   +
# Принимать приглашения в команд - Флаг +
# Верифицированный пользователь - Флаг +
# Рейтинг - Число
# Роль - Справочник "Роль пользователя" +
# Статус  - Справочник "Статус объекта" +



