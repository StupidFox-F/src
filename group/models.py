from django.db import models

from faker import Faker

# Create your models here.
class Group(models.Model):
    first_name = models.CharField(max_length=10, null=False)
    last_name = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.email}'

    @classmethod
    def generation_group(cls):
        fake = Faker()
        group = cls(
            first_name=fake.firt_name(),
            last_name=fake.last_name(),
            email=fake.email(),
        )
        group.save()
