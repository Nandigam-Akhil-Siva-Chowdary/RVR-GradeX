from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import StudentRecord, SubjectGrade
from decimal import Decimal

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            
            # Handle CGPA calculation
            if request.POST.get('calculation_type') == 'cgpa':
                sem1_gpa = Decimal(request.POST.get('sem1_gpa', 0))
                sem2_gpa = Decimal(request.POST.get('sem2_gpa', 0))
                student.sem1_gpa = sem1_gpa
                student.sem2_gpa = sem2_gpa
                student.cgpa = (sem1_gpa + sem2_gpa) / 2
                student.calculation_type = 'cgpa'
            
            # Handle SGPA calculation
            else:
                sgpa = Decimal(request.POST.get('sgpa', 0))
                student.sgpa = sgpa
                student.calculation_type = 'sgpa'
                
                # Save subject grades
                subjects_data = request.POST.getlist('subjects[]')
                grades_data = request.POST.getlist('grades[]')
                credits_data = request.POST.getlist('credits[]')
                
                # Save the student first to get the ID
                student.save()
                
                # Save each subject grade
                for i in range(len(subjects_data)):
                    if i < len(grades_data) and i < len(credits_data):
                        SubjectGrade.objects.create(
                            student=student,
                            subject_name=subjects_data[i],
                            subject_credit=Decimal(credits_data[i]),
                            grade=grades_data[i]
                        )
                
                return render(request, 'calculator/success.html', {'student': student})
            
            student.save()
            return render(request, 'calculator/success.html', {'student': student})
    else:
        form = StudentForm()
    return render(request, 'calculator/index.html', {'form': form})
