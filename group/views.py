from django.http import HttpResponse
from django.shortcuts import render
from group.models import Group

def groups_list(request):
    qs = Group.objects.all()

    if request.GET.get('fname'):
        qs = qs.filter(first_name=request.GET.get('fname'))

    if request.GET.get('lname'):
        qs = qs.filter(last_name=request.GET.get('lname'))

    if request.GET.get('email'):
        qs = qs.filter(email=request.GET.get('email'))

    result = '<br>'.join(
        str(group)
        for group in qs
    )
    return render(
        request=request,
        template_name='groups_list.html',
        context={'groups_list': result}
    )
