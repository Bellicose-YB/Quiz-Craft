import json
from django.db.models.query_utils import Q
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.cache import cache_control

from hashids import Hashids

from .models import Questions, Quiz, Student
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
            return redirect('starttest', quiz_id, hashids.encode(student_info.id))
    else:
        form = StudentForm()

    context = {
        'quiz': quiz,
        'form': form,
        'user_id': user_id,
        'quiz_id': quiz_id
    }

    return render(request, 'quiz_test_1.html', context)

def StartTestView(request, quiz_id, student_id):
    hashids = Hashids()
    decode_quiz_id = hashids.decode(quiz_id)
    decode_student_id = hashids.decode(student_id)
    quiz = Quiz.objects.get(pk=decode_quiz_id[0])
    student = Student.objects.get(pk=decode_student_id[0])

    return render(request, 'quiz_test_2.html', {'quiz': quiz, 'student': student})

def StartTestDataView(request, quiz_id, student_id):
    hashids = Hashids()
    decode_quiz_id = hashids.decode(quiz_id)
    quiz = Quiz.objects.get(pk=decode_quiz_id[0])

    Question = []
    for q in quiz.getQuestions():
        Que = {}
        Que['statement'] = q.Statement
        Que['Correct'] = q.CorrectOption
        Que['Other1'] = q.OtherOption1
        Que['Other2'] = q.OtherOption2
        Que['Other3'] = q.OtherOption3
        Que['Que_id'] = q.id
        Que['score'] = q.Score
        Question.append(Que)

    return JsonResponse({
        'question': Question,
        'time': quiz.Time,
        'student_id': student_id
    })

def CompleteTestView(request, student_id, score):
    hashids = Hashids()
    decode_score = hashids.decode(score)
    decode_student_id = hashids.decode(student_id)
    student = Student.objects.get(pk=decode_student_id[0])
    student.student_score = decode_score[0]
    student.done_test = True
    student.save()

    return render(request, 'complete-test.html')