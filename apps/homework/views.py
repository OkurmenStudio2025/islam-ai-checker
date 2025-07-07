from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import HomeworkResultsSerializer
from .models import HomeworkResults  # убедись, что эта модель подключена
from .services.homework_checker import sent_prompt_and_get_response, extract_grade_from_feedback
from rest_framework import viewsets



class HomeworkReviewCreateAPIView(APIView):
    def post(self, request):
        # Получаем данные из запроса
        student_name = request.data.get('student_name')
        group = request.data.get('group')  # предполагается ID
        task_title = request.data.get('task_title')
        task_condition = request.data.get('task_condition')
        student_answer = request.data.get('student_answer')

        # Проверка всех обязательных полей
        if not all([student_name, group, task_title, task_condition, student_answer]):
            return Response(
                {'error': 'Все поля обязательны: student_name, group, task_title, task_condition, student_answer'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Промпт для AI — отзыв на задание
        prompt_review = f"""
Ты — islam teacher ai. Твоя задача — проверить домашнее задание студента,
ученика 9–15 лет, который только начинает учиться.
Пиши отзыв от первого лица, как будто ты лично обращаешься к студенту.
Оцени работу по 10-балльной шкале. Max 70 слов.
Кратко и понятно объясни, что сделано правильно, а что — неправильно.
В конце дай итоговую оценку и комментарий в дружелюбном и вежливом стиле.
Условие задания: {task_condition}
Имя студента: {student_name}
Вот ответ студента: {student_answer}
"""

        # Промпт для AI — определение оригинальности
        prompt_originality = f"""
Ты — islam teacher ai. Проверь, сам ли студент (9–15 лет) написал это задание или использовал искусственный интеллект (например, ChatGPT).
Ответь строго одним словом: "Да" — если использовал ИИ, или "Нет" — если не использовал. Никаких объяснений.

Условие задания: {task_condition}
Имя: {student_name}
Ответ студента: {str(student_answer)}
"""


        # Отправка в AI
        ai_feedback = sent_prompt_and_get_response(prompt_review)
        originality_check = sent_prompt_and_get_response(prompt_originality)
        grade = extract_grade_from_feedback(ai_feedback)

        # Подготовка данных для сериализатора
        data = {
            'student_name': student_name,
            'group': group,
            'task_title': task_title,
            'task_condition': task_condition,
            'student_answer': student_answer,
            'ai_feedback': ai_feedback,
            'grade': grade,
            'originality_check': originality_check,
        }

        serializer = HomeworkResultsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = HomeworkResults.objects.all()
    serializer_class = HomeworkResultsSerializer
    http_method_names = ['get', 'head', 'options']
