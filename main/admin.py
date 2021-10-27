from django.contrib import admin

from .models import Question, Survey, VarAnswer, UserAnswers


admin.site.register(Question)
admin.site.register(Survey)
admin.site.register(VarAnswer)
admin.site.register(UserAnswers)
