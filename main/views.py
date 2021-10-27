from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from django.utils import timezone

from .models import Question, Survey, VarAnswer, UserAnswers

from .serializers import *


class AdminSurveyListView(APIView):
    """Вывод списка всех опросов для администратора"""
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        surveys = Survey.objects.all()
        serializer = AdminSurveyListSerializer(surveys, many=True)
        return Response(serializer.data)


class SurveyDetailView(generics.RetrieveAPIView):
    """Вывод детального описания опроса"""
    permission_classes = [permissions.AllowAny]
    queryset = Survey.objects.all()
    serializer_class = SurveyDetailSerializer


class CreateSurveyView(generics.CreateAPIView):
    """Создание опроса"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CreateSurveySerializer


class UpdateSurveyView(generics.UpdateAPIView):
    """Внесение изменений в существующий опрос"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Survey.objects.all()
    serializer_class = UpdateSurveySerializer

    def get(self, request, pk):
        survey = Survey.objects.get(id=pk)
        serializer = SurveyDetailSerializer(survey)
        return Response(serializer.data)


class DeleteSurveyView(generics.DestroyAPIView):
    """Удаление опроса"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Survey.objects.all()
    serializer_class = CreateSurveySerializer

    def get(self, request, pk):
        survey = Survey.objects.get(id=pk)
        serializer = SurveyDetailSerializer(survey)
        return Response(serializer.data)


class VarAnswerListView(generics.ListAPIView):
    """Вывод списка всех вариантов ответов"""
    permission_classes = [permissions.IsAdminUser]
    queryset = VarAnswer.objects.all()
    serializer_class = VarAnswerSerializer


class CreateVarAnswerView(generics.CreateAPIView):
    """Создание варианта ответа"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = VarAnswerSerializer


class UpdateVarAnswerView(generics.UpdateAPIView):
    """Изменение варианта ответа"""
    permission_classes = [permissions.IsAdminUser]
    queryset = VarAnswer.objects.all()
    serializer_class = VarAnswerSerializer

    def get(self, request, pk):
        var_answer = VarAnswer.objects.get(id=pk)
        serializer = VarAnswerSerializer(var_answer)
        return Response(serializer.data)


class DeleteVarAnswerView(generics.DestroyAPIView):
    """Удаление варианта ответа"""
    permission_classes = [permissions.IsAdminUser]
    queryset = VarAnswer.objects.all()
    serializer_class = VarAnswerSerializer

    def get(self, request, pk):
        var_answer = VarAnswer.objects.get(id=pk)
        serializer = VarAnswerSerializer(var_answer)
        return Response(serializer.data)


class QuestionListView(generics.ListAPIView):
    """Вывод всех вопросов"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Question.objects.all()
    serializer_class = DetailQuestionsSerializer


class CreateQuestionView(generics.CreateAPIView):
    """Создание вопроса и привязка его к опросу"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionSerializer


class UpdateQuestionView(generics.UpdateAPIView):
    """Изменение существующего вопроса"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, pk):
        question = Question.objects.get(id=pk)
        serializer = DetailQuestionsSerializer(question)
        return Response(serializer.data)


class DeleteQuestionView(generics.DestroyAPIView):
    """Удаление вопроса"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, pk):
        question = Question.objects.get(id=pk)
        serializer = DetailQuestionsSerializer(question)
        return Response(serializer.data)


class ActiveSurveyListView(generics.ListAPIView):
    """Вывод всех активных опросов"""
    permission_classes = [permissions.AllowAny]
    queryset = Survey.objects.all().filter(date_start__lte=timezone.now()).filter(date_finish__gt=timezone.now())
    serializer_class = UserSurveyListSerializer
    

class CreateUserAnswersView(generics.CreateAPIView):
    """Создание ответа пользователя на вопрос"""
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserAnswersSerializer


class ListUserSurveyView(APIView):
    """Вывод всех опросов и ответов пользователя"""
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        surveys = Survey.objects.filter(questions__usersSolution__user_id=pk).distinct()
        serializer = UserSurveySerializer(surveys, many=True, context={'id': pk})
        return Response(serializer.data)
