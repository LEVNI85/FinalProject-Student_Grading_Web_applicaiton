import pytest
from student_grading.models import Course, Lecturer, Subject

@pytest.mark.django_db
def test_subject_creation():
    course = Course.objects.create(name=1)
    lecturer = Lecturer.objects.create(name="Goga Bakhutadze", email="g_bakhutadze@edu.ge")
    subject = Subject.objects.create(name="Mathematics", course=course, lecturer=lecturer)

    assert Subject.objects.count() == 1
    assert subject.name == "Mathematics"
    assert subject.course == course
    assert subject.lecturer == lecturer
