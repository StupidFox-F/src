from django.core.management.base import BaseCommand
from student.models import Student


class Command(BaseCommand):
    help = 'Generation N students'

    def add_arguments(self, parser):
        parser.add_argument('n_students', default=100, type=int)

    def handle(self, *args, **kwargs):
        n_students = kwargs['n_students']
        for _ in range(n_students):
            # я так понимаю for _ in range не обязательна
            Student.generate_student()

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {n_students} students'))