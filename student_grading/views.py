from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Subject,Lecturer,Course,Student,Score
from .forms import SubjectForm, ScoreForm
from django.http import JsonResponse

@login_required
def subject_list(request):
    subjects = Subject.objects.select_related('course','lecturer')

    return render(request, 'subject_list.html', {'subjects':subjects})

@login_required
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Subject Created!")
            return redirect("subject_list")
    else:
        form = SubjectForm()

    return render(request, 'subject_form.html', {'form':form})

@login_required
def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk = pk)

    if request.method == 'POST':
        form = SubjectForm(request.POST, instance = subject)

        if form.is_valid():
            form.save()
            messages.success(request, "Subject Updated!")
            return redirect("subject_list")
    else:
        form = SubjectForm(instance = subject)

    return render(request, 'subject_form.html', {'form':form})

@login_required
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == "POST":
        subject.delete()
        messages.success(request, "Subject deleted!")
        return redirect("subject_list")

    return render(request, "subject_confirm_delete.html", {"subject": subject})

#------------------------------------
@login_required
def lecturer_list(request):
    lecturers = Lecturer.objects.all()
    return render(request, "lecturer_list.html", {"lecturers": lecturers})

@login_required
def student_list(request):
    students = Student.objects.select_related("course")
    return render(request, "student_list.html", {"students": students})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    scores = Score.objects.filter(student=student).select_related(
        "subject", "subject__course", "subject__lecturer"
    )

    data = []
    for s in scores:
        data.append({
            "id" : s.id,
            "subject": s.subject.name,
            "course": s.subject.course.name,
            "lecturer": f"{s.subject.lecturer.name} ({s.subject.lecturer.email})",
            "score": s.score,
        })

    return JsonResponse({"scores": data})

@login_required
def score_update(request, pk):
    score = get_object_or_404(Score, pk=pk)

    if request.method == "POST":
        form = ScoreForm(request.POST, instance=score)
        if form.is_valid():
            form.save()
            messages.success(request, f"Score updated for {score.student.name} in {score.subject.name}")
            return redirect('student_list')
    else:
        form = ScoreForm(instance=score)

    return render(request, 'score_form.html', {'form': form, 'score': score})