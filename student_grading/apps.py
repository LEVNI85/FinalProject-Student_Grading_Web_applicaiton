from django.apps import AppConfig


class StudentGradingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_grading'

    def ready(self):
        import student_grading.signals