from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer , AnswerSerializer
from app.models import Question, Answer


@api_view(['GET'])
def getAllData(request):
    raw = Question.objects.all()
    data = QuestionSerializer(raw, many=True)
    return Response(data.data)

@api_view(['GET'])
def getSpecificData(request, index):
    raw = Question.objects.filter(id=index).first()
    data = QuestionSerializer(raw, many=False)
    return Response(data.data)

@api_view(['GET'])
def getQuestionAnswerData(request, index):
    question = Question.objects.filter(id = index).first()
    raw = Answer.objects.filter(question_ref = question)
    data = AnswerSerializer(raw, many=True)
    return Response(data.data)