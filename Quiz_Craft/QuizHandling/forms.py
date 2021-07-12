from django import forms
from .models import Quiz, Questions


class QuizStarterForm(forms.ModelForm):
    score = forms.IntegerField(min_value=1, max_value=10000, required=False)
    class Meta:
        model = Quiz
        fields = ('QuizTitle', 'time', 'score')

class QuestionCreationForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'
