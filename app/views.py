from django.shortcuts import render, redirect
from django.http import HttpResponse, request, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from .forms import QuestionForm
from .models import Answer, Question

q_vote_token = 0
q_vote_answer_token = 0

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    question_answers = Answer.objects.filter(question_ref=question_id)
    context = {"question": question, "question_answers": question_answers}
    return render(request, "looking.html", context)

@require_POST
def vote_question(request):
    global q_vote_token
    q_vote_token += 1
    question_id = request.POST.get('question_id')
    question = get_object_or_404(Question, pk=question_id)
    if question.wasliked:
        question.votes -= 1
        question.wasliked = False
    else:
        question.votes += 1
        question.wasliked = True
    question.save()
    return JsonResponse({'votes': question.votes})

@require_POST
def vote_answer(request):
    global q_vote_answer_token
    q_vote_answer_token += 1
    answer_id = request.POST.get('question_id')
    question = get_object_or_404(Answer, pk=answer_id)
    if question.wasliked:
        question.votes -= 1
        question.wasliked = False
    else:
        question.votes += 1
        question.wasliked = True
    question.save()
    return JsonResponse({'votes': question.votes})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a page showing all questions
    else:
        form = QuestionForm()
    
    return render(request, 'posting.html', {'form': form})


import logging

logger = logging.getLogger(__name__)

@require_POST
def answer_question(request):
    logger.debug(f"Received POST data: {request.POST}")
    
    question_id = request.POST.get('question_ref')
    text = request.POST.get('text')

    # Print statements for debugging (optional)
    print(question_id)
    print(text)

    # Retrieve the Question instance
    question = get_object_or_404(Question, id=question_id)

    # Create the Answer instance
    answer = Answer.objects.create(question_ref=question, text=text)

    # Optionally, add more logic or return a response
    # For example, return a JSON response
    return JsonResponse({'status': 'success', 'answer_id': answer.id})

        