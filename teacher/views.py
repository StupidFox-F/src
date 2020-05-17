from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from teacher.forms import TeacherAddForm, TeacherEditForm
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


def teachers_edit(request, id):

    teachers_edit_template = 'edit_teacher.html'
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return HttpResponseNotFound(f"Teacher with id={id} doesn't exist")

    if request.method == 'POST':
        form = TeacherEditForm(request.POST or None, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teacher:list'))
    else:
        form = TeacherEditForm(instance=teacher)
    return render(request, teachers_edit_template,
                  {'form': form, 'title': 'Edit teacher'})


def delete_teacher(request, id):

    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return HttpResponseRedirect(reverse('teacher:list'))