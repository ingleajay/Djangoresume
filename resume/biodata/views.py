from .forms import ResumeForm
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import get_user_model

User = get_user_model()

show = None


def index(request):
    global show
    if request.method == 'POST':
        fr = ResumeForm(request.POST, request.FILES)
        if fr.is_valid():
            messages.success(request, 'Account created successfullly ')
            fr.save()
    else:
        fr = ResumeForm()
        show = User.objects.all()
    return render(request, 'index.html', {'form': fr, 'show': show})
