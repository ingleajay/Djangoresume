from django.shortcuts import render
from .forms import ResumeForm
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    if request.method == 'POST':
        fr = ResumeForm(request.POST, request.FILES)
        if fr.is_valid():
            messages.success(request, 'Account created successfullly ')
            fr.save()
    else:
        fr = ResumeForm()
    return render(request, 'index.html', {'form': fr})
