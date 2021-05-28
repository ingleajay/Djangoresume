from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django import forms
from biodata.forms import ResumeForm

User = get_user_model()
# Create your views here.

pic1 = None
pic = None


def create_resume(request):
    global pic1
    if request.user.is_authenticated:
        pic1 = User.objects.get(username=request.user)
    return render(request, 'resume.html', {'pic1': pic1})


def update_user(request):
    global pic
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = User.objects.get(username=request.user)
            pic1 = User.objects.get(username=request.user)
            fr = ResumeForm(request.POST, request.FILES, instance=pi)
            if fr.is_valid():
                messages.success(request, 'Data updated successfullly ')
                fr.save()
        else:
            pi = User.objects.get(username=request.user)
            pic = User.objects.get(username=request.user)
            pic1 = User.objects.get(username=request.user)
            fr = ResumeForm(instance=pi)
        return render(request, 'update.html', {'form': fr, 'pic': pic, 'pic1': pic1})
    else:
        return HttpResponseRedirect('/login/')
