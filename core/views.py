from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from . models import *

def index(request):
    questions = Question.objects.all()[0:5]
    return render(request, 'core/index.html', {'questions': questions})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Invalid Question')
    return render(request, 'core/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'core/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Question.DoesNotExist):
        return render(request, 'core/detail.html', {
            'question': question,
            'error_message': 'You didnt select a choice',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        messages.success(request, 'You just voted')
        return HttpResponseRedirect(reverse('core:results', args=(question.id,)))
