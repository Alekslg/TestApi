from django.urls import path
from . import views

urlpatterns = [
    path('admin/survey/', views.AdminSurveyListView.as_view(), name='admin_survey_list'),
    path('admin/survey/create/', views.CreateSurveyView.as_view()),
    path('admin/survey/update/<int:pk>/', views.UpdateSurveyView.as_view()),
    path('admin/survey/delete/<int:pk>/', views.DeleteSurveyView.as_view()),
    path('admin/var_answer/', views.VarAnswerListView.as_view()),
    path('admin/var_answer/create/', views.CreateVarAnswerView.as_view()),
    path('admin/var_answer/update/<int:pk>/', views.UpdateVarAnswerView.as_view()),
    path('admin/var_answer/delete/<int:pk>/', views.DeleteVarAnswerView.as_view()),
    path('admin/question/', views.QuestionListView.as_view()),
    path('admin/question/create/', views.CreateQuestionView.as_view()),
    path('admin/question/update/<int:pk>/', views.UpdateQuestionView.as_view()),
    path('admin/question/delete/<int:pk>/', views.DeleteQuestionView.as_view()),
    path('survey/', views.ActiveSurveyListView.as_view()),
    path('survey/<int:pk>/', views.SurveyDetailView.as_view()),
    path('answer/', views.CreateUserAnswersView.as_view()),
    path('list_user_survey/<int:pk>/', views.ListUserSurveyView.as_view()),
]

