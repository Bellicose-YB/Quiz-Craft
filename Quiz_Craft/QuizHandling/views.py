from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Quiz
from .forms import QuizStarterForm

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
    print(quiz)
    #@TODO CHECK HERE IF CURRENT QUIZ AUTHOR IS SAME AS OUR LOGIN USER

    #@TODO MAKE A FORM FOR QUESTIONS AND VALIDATE IT
    return render(request, 'make_questions.html')