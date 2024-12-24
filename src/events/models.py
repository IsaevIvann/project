#
# from django.db import models
# from src.users.models import User
#
# class MootCourt(models.Model):
#     created_at = models.DateTimeField(
#         auto_now_add=True
#         )
#     name = models.CharField(
#         max_length=255
#     )
#     organizer = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='organized_mootcourts'
#     )
#     pre_moot = models.ForeignKey(
#         'self',
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name='pre_moots'
#     )
#     type = models.ForeignKey(
#         'MootCourtType',
#         on_delete=models.PROTECT,
#         related_name='mootcourts'
#     )
#     tags = models.ManyToManyField(
#         'MootCourtTag',
#         related_name='mootcourts',
#         blank=True
#     )
#     message = models.ManyToManyField(
#         'Message',
#         related_name='mootcourts',
#         blank=True
#     )
#     events = models.ManyToManyField(
#         'Event',
#         related_name='mootcourts'
#     )
#     documents = models.ManyToManyField(
#         'Document',
#         related_name='mootcourts'
#     )
#     teams = models.ManyToManyField(
#         'Team',
#         related_name='mootcourts',
#         blank=True
#     )
#     senior_arbitrators = models.ManyToManyField(
#         User,
#         related_name='senior_arbitrator_mootcourts',
#         blank=True
#     )
#     arbitrators = models.ManyToManyField(
#         User,
#         related_name='arbitrator_mootcourts',
#         blank=True
#     )
#
#
#     requires_telegram_channel = models.BooleanField(default=False)
#     telegram_channel = models.OneToOneField(
#         'TelegramChannel',
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name='mootcourt',
#     )
#     status = models.ForeignKey(
#         'MootCourtStatus',
#         on_delete=models.PROTECT,
#         related_name='mootcourts'
#     )
#     background = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True
#     )
#     image = models.ImageField(
#         upload_to='mootcourt_images/',
#         blank=True,
#         null=True
#     )
#     object_status = models.ForeignKey(
#         'ObjectStatus',
#         on_delete=models.PROTECT,
#         related_name='mootcourts'
#     )
#
#     def __str__(self):
#         return self.name
#
