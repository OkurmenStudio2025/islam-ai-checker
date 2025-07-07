from django.db import models

class HomeworkResults(models.Model):
    student_name = models.CharField(
        max_length=100,
        verbose_name="Имя ученика",
        help_text="Введите имя и фамилию ученика"
    )
    group = models.ForeignKey(
        'group.Group',
        on_delete=models.CASCADE,
        related_name='homework_results',
        verbose_name="Группа",
        help_text="Выберите группу, к которой относится задание"
    )
    task_title = models.CharField(
        max_length=100,
        verbose_name="Название задания",
        help_text="Введите заголовок задания"
    )
    task_condition = models.TextField(
        verbose_name="Условие",
        help_text="Введите условие задания"
    )
    student_answer = models.TextField(
        verbose_name="Ответ ученика",
        help_text="Введите ответ, который дал ученик"
    )
    grade = models.FloatField(
        verbose_name="Оценка (из 10)",
        help_text="Оценка, выставленная за задание",
        null=True,
        blank=True
    )
    ai_feedback = models.TextField(
        verbose_name="Комментарий от Islam AI Checker",
        help_text="Отзыв или комментарий, сгенерированный cистемой Islam AI Checker",
        null=True,
        blank=True
    )
    originality_check = models.TextField(
        verbose_name="Анализ оригинальности",
        help_text="Проверка, сам ли ученик выполнил задание или использовал AI (например, ChatGPT)",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.student_name} — {self.task_title}"

    class Meta:
        verbose_name = "Результат задания"
        verbose_name_plural = "Результаты заданий"
