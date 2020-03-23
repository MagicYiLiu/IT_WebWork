from django.http import HttpResponse
from django.shortcuts import render
from secondPage.models import Student


# Create your views here.
def second(request):
    return HttpResponse("second page")


def add_student(request):
    student = Student()
    student.s_name = 'jerry'
    student.save()

    return HttpResponse("Add successful")


def get_student(request):
    students = Student.objects.all()
    for student in students:
        print(Student.s_name)

    # return HttpResponse("student list")
    context = {"hobby":"play Games"}
    return render(request, 'student_list.html',context=context)
