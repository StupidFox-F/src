from django.shortcuts import render
from faker import Faker
from django.http import HttpResponse
from student.models import Student

fake = Faker()

# Create your views here.
def student(request):
    result = []
    for _ in range(20):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        result.append({'First Name': first_name, 'Last Name': last_name, 'Email': email})
    return HttpResponse(result)




