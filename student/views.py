from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from faker import Faker
from django.http import HttpResponse, HttpResponseRedirect

from student.forms import StudentAddForm
from student.models import Student


# Create your views here.

def students_list(request):
    qs = Student.objects.all()

    q = Q()

    if request.GET.get('fname'):
        q &= Q(first_name=request.GET.get('fname'))

    if request.GET.get('lname'):
        q &= Q(last_name=request.GET.get('lname'))

    if request.GET.get('email'):
        q &= Q(email=request.GET.get('email'))

    qs = qs.filter(q)

    result = '<br>'.join(
        str(student)
        for student in qs
    )

    return render(
        request=request,
        template_name='students_list.html',
        context={'students_list': result}
    )


def students_add(request):

    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number').strip()
            email = form.cleaned_data.get('email').strip()

            is_student_exists = Student.objects.filter(Q(phone_number=phone_number) |
                                                       Q(email=email)).exists()
            if is_student_exists:
                error_massage = "Student not added. Student with such phone_number and email is exists! Try again:"
                return render(request, students_add, {'form': form, "error_massage": error_massage},
                              status=400)
            form.save()
            return HttpResponseRedirect(reverse('student'))
    else:
        form = StudentAddForm()

    return render(
        request=request,
        template_name='students_add.html',
        context={'form': form}
    )