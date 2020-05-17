from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from group.forms import GroupAddForm, GroupEditForm
from group.models import Group


def groups_list(request):
    qs = Group.objects.all()

    name = request.GET.get('name')
    specialty = request.GET.get('specialty')
    course_name = request.GET.get('course_name')

    groups_filter = Q()

    if name:
        groups_filter |= Q(name=name)
    if specialty:
        groups_filter |= Q(cours=specialty)
    if course_name:
        groups_filter |= Q(teacher=course_name)

    qs = qs.filter(groups_filter)

    return render(request, 'group/groups_list.html',
                  {'groups_list': qs, 'title': 'Group list'})


def groups_add(request):

    group_template = 'group_add.html'

    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            specialties = {
                "Cheef": ["cooking"],
                "Swimmer": ["Swimming"],
                "Football": ["Play"]
            }
            specialty = form.cleaned_data.get('specialty').strip()
            course_name = form.cleaned_data.get('course_name').strip()
            if specialty in ["Cheef", "Swimmer", "Football"]:
                if course_name not in specialties[specialty]:
                    error_message = "End"
                    return render(request, group_template, {'form': form, "error_message": error_message},
                                  status=400)
            else:
                error_message = "does not exist"
                return render(request, group_template, {'form': form, "error_message": error_message},
                              status=400)
            form.save()
            return HttpResponseRedirect(reverse('group:groups_list'))

    else:
        form = GroupAddForm()
    return render(request, group_template, {'form': form})

def groups_edit(request, id):

    edit_template = 'group_edit.html'
    try:
        group = Group.objects.get(id=id)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f"Group with id={id} doesn't exist")

    if request.method == 'POST':
        form = GroupEditForm(request.POST or None, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group:groups_list'))
    else:
        form = GroupEditForm(instance=group)
    return render(request, edit_template, {'form': form, 'title': 'Edit student'})


def delete_group(request, id):

    group = get_object_or_404(Group, id=id)
    group.delete()
    return HttpResponseRedirect(reverse('group:groups_list'))
