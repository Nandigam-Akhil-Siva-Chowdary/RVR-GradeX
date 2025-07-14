from django.contrib import admin
from .models import StudentRecord, SubjectGrade

class SubjectGradeInline(admin.TabularInline):
    model = SubjectGrade
    extra = 0

@admin.register(StudentRecord)
class StudentRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'reg_number', 'branch', 'calculation_type', 'get_result', 'created_at')
    list_filter = ('calculation_type', 'branch', 'created_at')
    search_fields = ('name', 'reg_number', 'branch')
    readonly_fields = ('created_at',)
    inlines = [SubjectGradeInline]
    
    fieldsets = (
        ('Student Information', {
            'fields': ('name', 'reg_number', 'branch', 'calculation_type')
        }),
        ('SGPA Calculation', {
            'fields': ('sgpa',),
            'classes': ('collapse',)
        }),
        ('CGPA Calculation', {
            'fields': ('sem1_gpa', 'sem2_gpa', 'cgpa'),
            'classes': ('collapse',)
        }),
        ('Record Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_result(self, obj):
        return obj.get_result()
    get_result.short_description = 'Result'

@admin.register(SubjectGrade)
class SubjectGradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject_name', 'subject_credit', 'grade')
    search_fields = ('student__name', 'subject_name', 'grade')
