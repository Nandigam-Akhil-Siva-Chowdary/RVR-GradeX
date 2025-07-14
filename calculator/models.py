from django.db import models

class StudentRecord(models.Model):
    CALCULATION_CHOICES = [
        ('sgpa', 'SGPA'),
        ('cgpa', 'CGPA'),
    ]
    
    name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    calculation_type = models.CharField(max_length=4, choices=CALCULATION_CHOICES, default='sgpa')
    
    # SGPA fields
    sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    
    # CGPA fields (2 semesters)
    sem1_gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem2_gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.reg_number}) - {self.calculation_type.upper()}"
    
    def get_result(self):
        """Return the calculated result based on calculation type"""
        if self.calculation_type == 'sgpa':
            return self.sgpa
        else:
            return self.cgpa

class SubjectGrade(models.Model):
    student = models.ForeignKey(StudentRecord, on_delete=models.CASCADE, related_name='subject_grades')
    subject_name = models.CharField(max_length=100)
    subject_credit = models.DecimalField(max_digits=4, decimal_places=2)
    grade = models.CharField(max_length=2)  # e.g., A+, A, B, etc.

    def __str__(self):
        return f"{self.student.name} - {self.subject_name}: {self.grade}"
