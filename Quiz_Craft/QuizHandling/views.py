from django.db.models.query_utils import Q
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Questions, Quiz
from .forms import QuizStarterForm,QuestionCreationForm

def Home(request):
    if request.method == "POST":
        form = QuizStarterForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.Author = request.user
            note.save()
            return redirect('createquestions', pk=note.id)
    else:
        form = QuizStarterForm()
    return render(request, 'home.html', {'form': form})



@login_required
def CreateQuestionsView(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    Question = []
    for q in quiz.getQuestions():
        Question.append(q)
    # print(Question)
    print("yath")
    if request.method == "POST":
        form = QuestionCreationForm(request.POST)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.AuthorKey = request.user
            ques.QuizKey = quiz
            ques.save()
            print("yatharth")
            return redirect('createquestions', pk=quiz.id)
            # return render(request, 'make_questions.html', {'form': form, 'Question' : Question, 'pk':pk})
    else:
        form = QuestionCreationForm()
    # print(quiz)
    #@TODO CHECK HERE IF CURRENT QUIZ AUTHOR IS SAME AS OUR LOGIN USER
    print("ystha")
    #@TODO MAKE A FORM FOR QUESTIONS AND VALIDATE IT
    return render(request, 'make_questions.html' ,{'form': form, 'pk' : pk,'Question' : Question})