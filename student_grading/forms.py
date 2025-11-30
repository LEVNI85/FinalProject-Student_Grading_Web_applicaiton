from django import forms
from .models import Score,Subject,Student,Course,Lecturer

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'course', 'lecturer']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-select'}),
            'course' : forms.Select(attrs={'class':'form-select'}),
            'lelcturer' : forms.Select(attrs={'class':'form-select'}),
        }

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['score']
        widgets = {
            'score': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
        }
