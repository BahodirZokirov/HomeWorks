from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

with open('/home/victus/Desktop/HomeWorks/lessons.txt', 'r') as lessons:
    lesson = lessons.readlines()
    all_lessons = [lessons.rstrip() for lessons in lesson]


def themes(request):
    context = {
        'lesson_table': all_lessons
    }
    return render(request, 'themes.html', context)


