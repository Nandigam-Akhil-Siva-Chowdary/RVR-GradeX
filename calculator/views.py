from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import StudentRecord

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return render(request, 'calculator/success.html', {'student': student})
    else:
        form = StudentForm()
    return render(request, 'calculator/index.html', {'form': form})
