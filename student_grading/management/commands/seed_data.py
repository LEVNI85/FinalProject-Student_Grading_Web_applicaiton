import random
from django.core.management.base import BaseCommand
from student_grading.models import Course, Lecturer, Subject, Student, Score
from faker import Faker

fake = Faker("ka_GE") 

class Command(BaseCommand):
    help = "Seed database with courses, lecturers, subjects, and students"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        if Course.objects.exists():
            self.stdout.write("Courses already created, skipping.")
        else:
            for i in range(1, 5):
                Course.objects.create(name=i)
            self.stdout.write("Courses 1-4 created.")

        if Lecturer.objects.count() >= 10:
            self.stdout.write("Lecturers already exist, skipping.")
        else:
            lecturers = []
            for _ in range(10):
                name = fake.first_name() + " " + fake.last_name()
                email = f"{name.split()[0][0].lower()}_{name.split()[1].lower()}@edu.ge"
                lecturer = Lecturer.objects.create(name=name, email=email)
                lecturers.append(lecturer)
            self.stdout.write("10 Lecturers created.")

        subjects_list = [
            "Algorithms", "Algorithms 2", "Kalkulusi", "Kalkulusi 2",
            "Diskretuli Matematika", "Wrifi Algebra", "Akademiuri Wera",
            "Monacemta Bazebi", "OOP", "Qselebi",
            "Operaciuli Sistemebi", "Manqanuri Swavleba", "AI",
            "Web Development", "Fizika", "Albatoba da Statistika"
        ]

        if Subject.objects.count() >= 20:
            self.stdout.write("Subjects already exist, skipping.")
        else:
            courses = list(Course.objects.all())
            lecturers = list(Lecturer.objects.all())
            if not courses or not lecturers:
                raise ValueError("No courses or lecturers available!")

            random.shuffle(lecturers)
            for i, name in enumerate(subjects_list):
                course = random.choice(courses)
                lecturer = lecturers[i % len(lecturers)]
    
                subject = Subject.objects.filter(name=name).first()
                if subject:
                    subject.lecturer = lecturer
                    subject.save()
                else:
                    Subject.objects.create(name=name, course=course, lecturer=lecturer)

        if Student.objects.count() >= 10:
            self.stdout.write("Students already exist, skipping.")
        else:
            courses = list(Course.objects.all())
            subjects = list(Subject.objects.all())

            for _ in range(10):
                course = random.choice(courses)
                name = fake.first_name() + " " + fake.last_name()
                student = Student.objects.create(name=name, course=course)

                course_subjects = [s for s in subjects if s.course == course]
                if not course_subjects:
                    raise ValueError(f"No subjects available for course {course.name}")

                assigned = random.sample(course_subjects, k=min(len(course_subjects), random.randint(2,5)))
                student.subjects.add(*assigned)

                for subj in assigned:
                    Score.objects.create(student=student, subject=subj, score=random.randint(50,100))

            self.stdout.write("10 Students created with subjects and scores.")

        self.stdout.write(self.style.SUCCESS("Seeding complete!"))
