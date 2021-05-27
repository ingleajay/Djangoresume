from .forms import ResumeForm, LoginForm
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import views as auth_views

User = get_user_model()

show = None
show1 = None
pic = None
pic1 = None


def index(request):
    return render(request, 'index.html')


def register(request):
    global show
    if request.method == 'POST':
        fr = ResumeForm(request.POST, request.FILES)
        if fr.is_valid():
            messages.success(request, 'Account created successfullly ')
            fr.save()
            fr = ResumeForm()
    else:
        fr = ResumeForm()
        show = User.objects.all()
    return render(request, 'register.html', {'form': fr, 'show': show})


def delete_user(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def view_user(request, id):
    global show1
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fr = ResumeForm(request.POST, request.FILES, instance=pi)
        if fr.is_valid():
            messages.success(request, 'Data updated successfullly ')
            fr.save()
    else:
        pi = User.objects.get(pk=id)
        show1 = User.objects.get(id=id)
        fr = ResumeForm(instance=pi)
        return render(request, 'view.html', {'form': fr, 'show1': show1, })


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fl = LoginForm(request=request, data=request.POST)
            if fl.is_valid():
                uname = fl.cleaned_data['username']
                upass = fl.cleaned_data['password']
                # request.session['name'] = uname
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You login Successfully  ')
                    return HttpResponseRedirect('/resume/')
        else:
            fl = LoginForm()
        return render(request, 'login.html', {'form': fl})
    else:
        return HttpResponseRedirect('/resume/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


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
            fr = ResumeForm(request.POST, request.FILES, instance=pi)
            if fr.is_valid():
                messages.success(request, 'Data updated successfullly ')
                fr.save()
        else:
            pi = User.objects.get(username=request.user)
            pic = User.objects.get(username=request.user)
            fr = ResumeForm(instance=pi)
        return render(request, 'update.html', {'form': fr, 'pic': pic, })
    else:
        return HttpResponseRedirect('/login/')
