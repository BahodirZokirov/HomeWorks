from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    return HttpResponse("<h1>Assalomu alaykum bosh sahifaga xush kelibsiz</h1>"
                        "(1-topshiriq)<br> <a href = 'themes/'>Themes</a> <br><hr>"
                        "(2-topshiriq)<br> <a href = 'pupils'>Pupils<a/> <br><hr>"
                        "(2.a- topshiriq)<br><a href ='pupils/grades'>Grades</a>")