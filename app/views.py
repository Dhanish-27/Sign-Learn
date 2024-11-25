from django.shortcuts import render,redirect
from django.views import View
from googletrans import Translator
from .models import *
from .quiz import play_game
from django.contrib.auth.models import User

class sign(View):
    string = ""
    quiz=""
   
    @classmethod
    def returnchar(cls, char):
        if char=="none":
            cls.string=""
            return cls.string
        cls.string += char
        return cls.string    
    @classmethod
    def returnquiz(cls,opt):
        cls.quiz=opt
        return cls.quiz

def index(request):
    return render(request,"new/1stpge.html")

def alphabets(request):
    return render(request,"new/alphabets.html")
def alpha(request, char):
    name = sign.returnchar(char)
    if char=="none":
        name=None
        return render(request, "new/alphabets.html",{"name":name})
    return render(request, "new/alphabets.html",{"name":name})

def image(request,name):
    return render(request, "new/imggenerator.html",{"name":name})

def translation(request,name):
    lang=request.GET.get("selection")
    print(lang)
    if lang is not None:
        translator=Translator() 
        translation = translator.translate(name, dest=lang)
        translated= translation.text
        return render(request,"new/translator.html",{"name":name,"translated":translated})
    else:
        return render(request, "new/translator.html",{"name":name})

def texttosign(request):
    if request.method=="GET":
        text1=request.GET.get("searchbox")
        if text1 is not None:
            translator=Translator()
            translation = translator.translate(text1, dest="en")
            translated= translation.text
            translated=translated.upper()
            lis = [char + ".jpg" for char in translated if char != ' ']
            return render(request,"new/texttosign.html",{"text":lis})
    return render(request,"new/texttosign.html")

def texttospeech(request,name):
    name=name.lower()
    return render(request,"texttospeech.html",{"name":name})

def leader(request):
    obj=leader2.objects.order_by("-points")
    length=[x+1 for x in range(len(obj))]
    return render(request,"new/leaderboard.html",{"obj":obj,"length":length})

def quizgame(request):
    correct_answer, options = play_game()
    correct_answer_img = correct_answer + ".jpg"
    return render(request, 'new/quizgame.html', {"crtans": correct_answer_img, "options": options, "ans": correct_answer})

def quiz_result(request, answer):
    if request.method == 'POST':
        ans_img = answer + ".jpg"
        answer2 = request.POST.get('answer')
        if answer == answer2:
            current_user = request.user
            username = current_user.username
            try:
                crt_user_object = leader2.objects.get(name=username)
            except leader2.DoesNotExist:
                crt_user_object = leader2.objects.create(name=username, points=0)
            crt_user_object.points += 1
            crt_user_object.save()
            return render(request, 'new/quizresult.html', {"crtans": ans_img, "res": "correct"})
        else:
            return render(request, 'new/quizresult.html', {"crtans": ans_img, "res": None})