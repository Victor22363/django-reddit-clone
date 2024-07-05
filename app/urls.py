from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

    path('vote/', views.vote_question, name='vote_question'),
    path('vote-answer/', views.vote_answer, name='vote_answer'),
    
    path('ask/', views.ask_question, name='ask_question'),
    path('answer/', views.answer_question, name='answer_question'),
]