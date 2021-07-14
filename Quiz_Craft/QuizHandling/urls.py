from django.urls import path, include
from .views import Home, CreateQuestionsView, QuizTestView, StartTestView, StartTestDataView, CompleteTestView

urlpatterns = [
    path('', Home, name='home'),
    path('question/<int:pk>', CreateQuestionsView, name="createquestions"),
    path('quiz-test/<str:user_id>/<str:quiz_id>', QuizTestView, name="quiztest"),
    path('start-test/<str:quiz_id>/<str:student_id>', StartTestView, name="starttest"),
    path('start-test/<str:quiz_id>/<str:student_id>/data', StartTestDataView, name="startdatatest"),
    path('complete-test/<str:student_id>/<str:score>', CompleteTestView, name="completetest")
] 