import json
from django.db.models.query_utils import Q
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers

from hashids import Hashids

from .models import Questions, Quiz
from .forms import QuizStarterForm, QuestionCreationForm, StudentForm

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
    hashids = Hashids()
    quiz = Quiz.objects.get(pk=pk)
    Question = []
    for q in quiz.getQuestions():
        Question.append(q)

    if request.method == "POST":
        form = QuestionCreationForm(request.POST)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.AuthorKey = request.user
            ques.QuizKey = quiz
            ques.save()
            return redirect('createquestions', pk=quiz.id)
    else:
        form = QuestionCreationForm()

    user = request.user.id
    #@TODO CHANGE WHEN DEPLOY
    BASE_URL =  'http://127.0.0.1:8000/quiz-test/' + hashids.encode(user) + '/' + hashids.encode(pk)

    context = {
        'form': form,
        'pk': pk,
        'Question': Question,
        'link': BASE_URL
    }
    return render(request, 'make_questions.html', context)

def QuizTestView(request, user_id, quiz_id):
    hashids = Hashids()
    decode_quiz_id = hashids.decode(quiz_id)
    decode_user_id = hashids.decode(user_id)
    owner = User.objects.get(id=decode_user_id[0])
    quiz = Quiz.objects.get(pk=decode_quiz_id[0])

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student_info = form.save(commit=False)
            student_info.student_score = 0
            student_info.quiz = quiz
            student_info.save()
            return redirect('starttest', quiz_id)
    else:
        form = StudentForm()

    context = {
        'quiz': quiz,
        'form': form,
        'user_id': user_id,
        'quiz_id': quiz_id
    }

    return render(request, 'quiz_test_1.html', context)

def StartTestView(request, quiz_id):
    hashids = Hashids()
    decode_quiz_id = hashids.decode(quiz_id)
    quiz = Quiz.objects.get(pk=decode_quiz_id[0])

    return render(request, 'quiz_test_2.html', {'quiz': quiz})

def StartTestDataView(request, quiz_id):
    hashids = Hashids()
    decode_quiz_id = hashids.decode(quiz_id)
    quiz = Quiz.objects.get(pk=decode_quiz_id[0])

    Question = []
    for q in quiz.getQuestions():
        Question.append(q)

    tmpJson = serializers.serialize("json", Question)
    tmpObj = json.loads(tmpJson)

    return JsonResponse({
        'question': json.dumps(tmpObj),
    })
