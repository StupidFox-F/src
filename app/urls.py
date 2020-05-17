"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student.views import students_list, students_add, students_edit
from teacher.views import teachers_list, teachers_add
from group.views import groups_list


urlpatterns = {
    path('admin/', admin.site.urls),
    path('student/', students_list, name='student'),
    path('teacher/', teachers_list, name='teacher'),
    path('group/', groups_list),
    path('teacher/add/', teachers_add),
    path('student/add/', students_add),
    path('student/edit/<int:id>', students_edit),
}
