from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllData, name='getAllData'),
    path('filter/<int:index>', views.getQuestionAnswerData, name='getFilteredData'),
    path('<int:index>/', views.getSpecificData, name='getSpecificData'),
]