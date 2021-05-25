from .forms import ResumeForm
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import get_user_model

User = get_user_model()

show = None
show1 = None


def index(request):
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
    return render(request, 'index.html', {'form': fr, 'show': show})


def delete_user(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def update_user(request, id):
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
    return render(request, 'update.html', {'form': fr, 'show1': show1, })
