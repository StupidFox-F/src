from django.db import models

# Create your models here.
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=10, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.email}, {self.phone_number}'

    @classmethod
    def generation_teacher(cls):
        faker = Faker()

        teacher = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            phone_number=faker.phone_number()
        )
        teacher.save()
