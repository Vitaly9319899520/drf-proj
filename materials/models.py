from django.db import models


class Lesson(models.Model):
    title = models.CharField(
        max_length=35,
        verbose_name="Название",
        help_text="Укажите урок",
    )

    preview = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Укажите превью",
    )

    description = models.TextField(
        blank=True, null=True, verbose_name="Опишите урок", help_text="Укажите описание"
    )

    video_url = models.URLField(max_length=200)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Course(models.Model):
    title = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Название",
        help_text="Укажите курс",
    )

    preview = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Укажите превью",
    )

    description = models.TextField(
        blank=True, null=True, verbose_name="Опишите курс", help_text="Укажите описание"
    )

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="Урок",
        help_text="Выберите урок",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
