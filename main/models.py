from django.db import models


class Survey(models.Model):
    """Описание модели опроса"""
    title = models.CharField(max_length=255, verbose_name="Название")
    date_start = models.DateField(verbose_name="Дата старта")
    date_finish = models.DateField(verbose_name="Дата окончания")
    description = models.TextField(verbose_name="Описание")

    def save(self, *args, **kwargs):
        """Exclude the possibility of changing start date"""
        if self.pk is not None:
            original = Survey.objects.get(pk=self.pk)
            self.date_start = original.date_start
        super(Survey, self).save(*args, **kwargs)

    def __str__(self):
        return '{0}'.format(self.title)

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class VarAnswer(models.Model):
    """Вариант ответа на вопрос в опросе"""
    title = models.TextField(unique=True, verbose_name="Текст ответа")

    def __str__(self):
        return '{0}'.format(self.title)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Варианты ответов"


class Question(models.Model):
    """Вопрос в опросе"""
    ANSWERS = (
        ('T', 'ответ текстом'),
        ('O', 'ответ с выбором одного варианта'),
        ('M', 'ответ с выбором нескольких вариантов'),
    )
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions', verbose_name="Опрос")
    title = models.CharField(max_length=512, verbose_name="Текст вопроса")
    type_answers = models.CharField(max_length=1, choices=ANSWERS, blank=False, verbose_name="Тип ответа")
    answers = models.ManyToManyField(VarAnswer, related_name='Question', blank=True, verbose_name="Варианты ответов")

    def __str__(self):
        return '{0}'.format(self.title)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы для опросов"


class UserAnswers(models.Model):
    """Пользовательский ответ на вопрос в опросе"""
    user_id = models.PositiveIntegerField(verbose_name="ID анонимного пользователя")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='usersSolution',
                                 verbose_name="Вопрос")
    answer = models.TextField(blank=True, verbose_name="Текстовый ответ")
    answers = models.ManyToManyField(VarAnswer, related_name='UsersSolution', blank=True,
                                     verbose_name="Выбранные варианты ответа")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата прохождения опроса")

    def __str__(self):
        return f"{self.user_id} {self.survey.title} {self.question.title}"

    class Meta:
        verbose_name = "Ответ пользователя на вопрос"
        verbose_name_plural = "Ответы пользователя на вопрос в опросе"
