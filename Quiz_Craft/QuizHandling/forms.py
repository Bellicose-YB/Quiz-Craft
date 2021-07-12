from django import forms
from .models import Quiz, Questions


class QuizStarterForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionCreationForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'
