from django.db import models


class Course(models.Model):
    course_name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    course_description = models.TextField(
        verbose_name="Описание курса",
        help_text="Введите описание курса",
        blank=True,
        null=True,
    )
    course_picture = models.ImageField(
        upload_to="materials/photo",
        blank=True,
        null=True,
        verbose_name="Превью курса",
        help_text="Загрузите картинку курса",
    )
    student = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='студент курса',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    lesson_name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    lesson_description = models.TextField(
        verbose_name="Описание урока",
        help_text="Введите описание урока",
        blank=True,
        null=True,
    )
    lesson_picture = models.ImageField(
        upload_to="materials/photo",
        blank=True,
        null=True,
        verbose_name="Превью урока",
        help_text="Загрузите картинку урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Введите название курса",
        null=True,
        blank=True,
        related_name="lessons",
    )
    video_link = models.URLField(
        max_length=300,
        verbose_name="Ссылка на видео",
        help_text="Добавьте ссылку на видео",
        null=True,
        blank=True,
    )
    student = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='студент урока',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"