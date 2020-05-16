from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from teacher.forms import TeacherAddForm
from teacher.models import Teacher


# Create your views here.

def teachers_list(request):
    qs = Teacher.objects.all()

    q = Q()

    if request.GET.get('fname'):
        q &= Q(first_name=request.GET.get('fname'))

    if request.GET.get('lname'):
        q &= Q(last_name=request.GET.get('lname'))

    if request.GET.get('email'):
        q &= Q(email=request.GET.get('email'))

    qs = qs.filter(q)

    result = '<br>'.join(
        str(teacher)
        for teacher in qs
    )

    # return HttpResponse(result)
    return render(
        request=request,
        template_name='teachers_list.html',
        context={'teachers_list': result}
    )


def teachers_add(request):

    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number').strip()
            email = form.cleaned_data.get('email').strip()

            is_teacher_exists = Teacher.objects.filter(Q(phone_number=phone_number) |
                                                       Q(email=email)).exists()
            if is_teacher_exists:
                error_massage = "Teacher not added. Teacher with such phone_number and email is exists! Try again:"
                return render(request, teachers_add, {'form': form, "error_massage": error_massage},
                              status=400)
            form.save()
            return HttpResponseRedirect(reverse('teacher'))
    else:
        form = TeacherAddForm()

    return render(
        request=request,
        template_name='teachers_add.html',
        context={'form': form}
    )
