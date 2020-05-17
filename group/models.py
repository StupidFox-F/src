import random

from django.db import models

from faker import Faker

# Create your models here.
from teacher.models import Teacher


class Group(models.Model):
    name = models.CharField(max_length=70, null=True)
    course = models.CharField(max_length=128, null=True)
    teacher = models.ForeignKey(to=Teacher, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} - {self.course}'

    @classmethod
    def generate_group(cls):

        course_n = None

        spesial = random.choice(["Cheef", "Swimmer", "Football"])

        if spesial == 'Cheef':
            course_n = ["cooking"]
        elif spesial == 'Swimmer':
            course_n = ["Swimming"]
        elif spesial == 'Football':
            course_n = ["Player"]
        courses_name = random.choice(course_n)

        group = cls(
            name=f'Group - {random.choice(range(10))}',
            courses_name=courses_name,
            spesial=spesial
        )
        group.save()
