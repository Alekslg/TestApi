from rest_framework import serializers

from .models import Question, Survey, VarAnswer, UserAnswers


class VarAnswerSerializer(serializers.ModelSerializer):
    """Вывод списка всех вариантов ответов на вопросы"""
    class Meta:
        model = VarAnswer
        fields = "__all__"


class DetailQuestionsSerializer(serializers.ModelSerializer):
    """Вывод подробного описания вопроса с типом ответа и предложенными вариантами"""
    type_answers = serializers.StringRelatedField(source='get_type_answers_display')
    answers = VarAnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        exclude = ('survey',)


class AdminSurveyListSerializer(serializers.ModelSerializer):
    """Вывод для администратора списка всех опросов в БД"""
    class Meta:
        model = Survey
        fields = "__all__"


class UserSurveyListSerializer(serializers.ModelSerializer):
    """Вывод для пользователя списка всех активных опросов на данный момент времени"""
    class Meta:
        model = Survey
        fields = ("id", "title", "description")


class SurveyDetailSerializer(serializers.ModelSerializer):
    """Детальное описание опроса с выводом предложенных вопросов и вариантов ответа"""
    questions = DetailQuestionsSerializer(read_only=True, many=True)

    class Meta:
        model = Survey
        fields = "__all__"


class CreateSurveySerializer(serializers.ModelSerializer):
    """Создание опроса"""
    class Meta:
        model = Survey
        fields = "__all__"


class UpdateSurveySerializer(serializers.ModelSerializer):
    """Внесение изменений в опрос, редактирование даты старта запрещено"""
    class Meta:
        model = Survey
        fields = "__all__"
        read_only_fields = ('date_start',)


class QuestionSerializer(serializers.ModelSerializer):
    """Сериалайзер вопроса для опроса, с представлением удобочитаемого значения типа ответа"""
    # type_answers = serializers.StringRelatedField(source='get_type_answers_display')
    class Meta:
        model = Question
        fields = "__all__"


class FiltrSerializer(serializers.ListSerializer):
    """Филтр QuerySet для вывода ответов на вопрос от конкретного пользователя"""
    def to_representation(self, data):
        data = data.filter(user_id=self.context.get("id"))
        return super(FiltrSerializer,  self).to_representation(data)


class UserVarAnswerSerializer(serializers.ModelSerializer):
    """Краткий вывод варианта ответа для представлении в списке пройденных пользователем опросов"""
    class Meta:
        model = VarAnswer
        fields = ['title']


class CreateUserAnswersSerializer(serializers.ModelSerializer):
    """Создание ответа пользователя на вопрос из опроса"""
    class Meta:
        model = UserAnswers
        fields = "__all__"


class UserAnswersSerializer(serializers.ModelSerializer):
    """Вывод ответов пользователя в списке пройденных опросов"""
    answers = UserVarAnswerSerializer(read_only=True, many=True)

    class Meta:
        list_serializer_class = FiltrSerializer
        model = UserAnswers
        fields = ['answer', 'answers', 'date']


class UserQuestionsSerializer(serializers.ModelSerializer):
    """Вывод вопросоов и ответов пользователя в списке пройденных опросов"""

    type_answers = serializers.StringRelatedField(source='get_type_answers_display')
    usersSolution = UserAnswersSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'type_answers', 'usersSolution']


class UserSurveySerializer(serializers.ModelSerializer):
    """Вывод опроса с ответом пользователя"""
    questions = UserQuestionsSerializer(read_only=True, many=True)

    class Meta:
        model = Survey
        fields = ['id', 'title', 'description', 'questions']
