from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
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
    '''f_name = request.GET.get('fname')
    l_name = request.GET.get('lname')
    e_mail = request.GET.get('email')

    if f_name:
        qs = qs.filter(Q(first_name=f_name))
    if l_name:
        qs = qs.filter(Q(last_name=l_name))
    if e_mail:
        qs = qs.filter(Q(email=e_mail))'''

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


'''
qs = Teacher.objects.all()
    search = request.GET.get('fname')
    if search:
        qs = qs.filter(Q(first_name='fname') | Q(last_name='lname') | Q(email='email'))
        
 if request.GET.get('fname'):
        qs = qs.filter(first_name=request.GET.get('fname'))

    if request.GET.get('lname'):
        qs = qs.filter(last_name=request.GET.get('lname'))

    if request.GET.get('email'):
        qs = qs.filter(email=request.GET.get('email'))
'''