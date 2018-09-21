from django.shortcuts import render, get_object_or_404
from django.http import Http404

# from django.http import HttpResponse

from .models import Course, Step


# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {
        'courses': courses
    })


def course_detail(request, pk):
    # course = get_object_or_404(Course, pk=pk)
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return render(request, "404.html")
    else:
        return render(request, "courses/course_detail.html", {'course': course})


def step_detail(request, course_pk, step_pk):
    try:
        step = Step.objects.get(course=course_pk, pk=course_pk)
    except Step.DoesNotExist:
        render(request, "404.html")
    else:
        return render(request, "courses/step_detail.html", {'step': step})
