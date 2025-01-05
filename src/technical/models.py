
from django.db import models


class Message(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата публикации"
    )
    author = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name="sent_messages",
        verbose_name="Автор"
    )
    text = models.TextField(
        verbose_name="Текст"
    )
    recipient = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name="received_messages",
        verbose_name="Получатель"
    )
    document = models.FileField(
        upload_to="documents/",
        blank=True, null=True,
        verbose_name="Документ"
    )

    def __str__(self):
        return f"Сообщение от {self.author} к {self.recipient} ({self.created_at})"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Document(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    author = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name="documents",
        verbose_name="Автор"
    )
    type = models.CharField(
        max_length=100,
        verbose_name="Тип документа"
    )
    file_name = models.CharField(
        max_length=255,
        verbose_name="Название файла"
    )
    icon = models.ImageField(
        upload_to="document_icons/",
        blank=True, null=True,
        verbose_name="Иконка")
    file = models.FileField(
        upload_to="documents/",
        verbose_name="Файл")

    def __str__(self):
        return f"{self.file_name} ({self.type})"

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"


class Documents(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания")
    author = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name="docs",
        verbose_name="Автор"
    )
    type = models.CharField(
        max_length=100,
        verbose_name="Тип документа"
    )
    file_name = models.CharField(
        max_length=255,
        verbose_name="Название файла"
    )
    icon = models.ImageField(
        upload_to="documents_icons/",
        blank=True, null=True,
        verbose_name="Иконка"
    )
    file = models.FileField(
        upload_to="documents/",
        verbose_name="Файл")

    def __str__(self):
        return f"{self.file_name} ({self.type})"

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


