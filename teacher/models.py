from django.db import models

# Create your models here.
from faker import Faker, factory
from faker.providers import phone_number


class Teacher(models.Model):
    first_name = models.CharField(max_length=10, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.email}'

    @classmethod
    def generation_teacher(cls):
        fake = Faker()

        teacher = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
        )
        teacher.save()
