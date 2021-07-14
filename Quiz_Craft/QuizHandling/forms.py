from django import forms
from .models import Quiz, Questions, Student


class QuizStarterForm(forms.ModelForm):
    QuizTitle = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class' : "form-control", 'placeholder': 'Title of Quiz'}))
    Time = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class' : "form-control", 'placeholder': 'Duration in minutes'}))
    Score = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'placeholder': 'Total score of Quiz'}))
    class Meta:
        model = Quiz
        fields = ('QuizTitle', 'Time', 'Score')

class QuestionCreationForm(forms.ModelForm):
    Score = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class' : "form-control", 'placeholder': 'Score of this question'}))
    Statement = forms.CharField(required=True, widget=forms.Textarea(attrs={'class' : "form-control", 'placeholder': 'Stament of Question'}))
    CorrectOption = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(attrs={'class' : "form-control"}))
    OtherOption1 = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(attrs={'class' : "form-control"}))
    OtherOption2 = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(attrs={'class' : "form-control"}))
    OtherOption3 = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(attrs={'class' : "form-control"}))
    class Meta:
        model = Questions
        fields = ('Statement','Score', 'CorrectOption', 'OtherOption1', 'OtherOption2', 'OtherOption3')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_name', 'student_email')
