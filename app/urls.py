from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alphabets',views.alphabets,name="alphabets"),
    path('select/<str:char>',views.alpha,name="alpha"),
    path('image/<str:name>',views.image,name="image"),
    path('translator/<str:name>',views.translation,name="translator"),
    path('texttosign',views.texttosign,name="texttosign"),
    path('texttospeech/<str:name>',views.texttospeech,name="texttospeech"),
    path('leaderboard',views.leader,name="leaderboard"),
    path('quizgame',views.quizgame,name="quizgame"),
    path('quizresult/<str:answer>',views.quiz_result,name="quizresult"),
]
