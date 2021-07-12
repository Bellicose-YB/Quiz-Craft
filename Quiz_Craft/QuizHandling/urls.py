from django.urls import path, include
from .views import Home, CreateQuestionsView, QuizTestView, StartTestView, StartTestDataView

urlpatterns = [
    path('', Home, name='home'),
    path('question/<int:pk>', CreateQuestionsView, name="createquestions"),
    path('quiz-test/<str:user_id>/<str:quiz_id>', QuizTestView, name="quiztest"),
    path('start-test/<str:quiz_id>', StartTestView, name="starttest"),
    path('start-test/<str:quiz_id>/data', StartTestDataView, name="startdatatest")
] 