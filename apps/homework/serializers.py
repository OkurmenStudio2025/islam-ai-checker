from rest_framework import serializers
from .models import HomeworkResults

class HomeworkResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkResults
        fields = [
            'id',
            'student_name',
            'group',
            'task_title',
            'task_condition',
            'student_answer',
            'grade',
            'ai_feedback',
            'originality_check',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']
