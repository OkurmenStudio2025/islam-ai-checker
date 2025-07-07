from django.db import models


class Group(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название группы",
        help_text="Введите название группы (например, A-1, Python Kids и т.д.)"
    )
    telegram_id = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Telegram ID группы",
        help_text=(
            "Введите Telegram ID группы, если есть (для отправки сообщений)"
            )
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["name"]

    def __str__(self):
        return self.name
