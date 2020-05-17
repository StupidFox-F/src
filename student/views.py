from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from faker import Faker
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from student.forms import StudentAddForm, StudentEditForm
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
        context={'students_list': result,
                 'student_list' : 'Add Student'
                 }
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
        context={'form': form,
                 'tittle': 'Add Students'}
    )


def students_edit(request, id):

    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Student with id{id} doesn`t exist")

    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)

        if form.is_valid():
            student = form.save()
            print(f'Student created: {student}')
            return HttpResponseRedirect(reverse('student'))
    else:
        form = StudentEditForm(
            instance=student
        )

    return render(
         request=request,
         template_name='students_edit.html',
         context={'form': form,
                  'title': 'Student_edit'}
    )

def student_delete(request, id):

    student = get_object_or_404(Student, id=id)
    student.delete()
    return HttpResponseRedirect(reverse('student'))
