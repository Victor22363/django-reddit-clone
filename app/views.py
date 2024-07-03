from django.shortcuts import render
from django.http import HttpResponse, request

from .models import Answer, Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    question_answers = Answer.objects.filter(question_ref=question_id)
    context = {"question": question, "question_answers": question_answers}
    return render(request, "looking.html", context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
