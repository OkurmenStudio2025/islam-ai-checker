from django.contrib import admin
from .models import HomeworkResults


@admin.register(HomeworkResults)
class HomeworkResultsAdmin(admin.ModelAdmin):
    list_display = (
        "student_name", 
        "group", 
        "task_title", 
        "grade", 
        "short_ai_feedback"
    )
    search_fields = (
        "student_name", 
        "task_title", 
        "group__name"
    )
    ordering = ("-id",)
    list_filter = ("grade", "group")

    readonly_fields = ("grade", "ai_feedback", "originality_check")

    fieldsets = (
        ("Информация об ученике", {
            "fields": ("student_name", "group"),
        }),
        ("Информация о задании", {
            "fields": ("task_title", "task_condition", "student_answer"),
        }),
        ("Результаты проверки", {
            "fields": ("grade", "ai_feedback", "originality_check"),
        }),
    )

    def short_ai_feedback(self, obj):
        return (obj.ai_feedback[:75] + "...") if len(obj.ai_feedback) > 75 else obj.ai_feedback

    short_ai_feedback.short_description = "AI отзыв"
