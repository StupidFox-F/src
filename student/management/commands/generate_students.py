from django.core.management.base import BaseCommand
from student.models import Student
from faker import Faker

class Command(BaseCommand):
    help = 'Generation N students'

    def add_arguments(self, parser):
        parser.add_argument('n_students', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        n_students = kwargs['n_students']

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {n_students} students'))