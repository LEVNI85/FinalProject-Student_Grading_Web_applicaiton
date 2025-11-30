from django.contrib import admin
from django import forms
from .models import Lecturer, Course, Student, Subject, Score

class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.course_id:
            self.fields['subjects'].queryset = Subject.objects.filter(
                course=self.instance.course
            )
        else:
            self.fields['subjects'].queryset = Subject.objects.none()

class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm

admin.site.register(Lecturer)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Score)
admin.site.register(Student, StudentAdmin)   
