from django.urls import path, include
from .views import Home, CreateQuestionsView

urlpatterns = [
    path('', Home, name='home'),
    path('question/<int:pk>', CreateQuestionsView, name="createquestions")
] 