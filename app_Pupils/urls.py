from django.urls import path
from .views import students, grades

urlpatterns = [
    path("", students, name='students'),
    path("grades/", grades, name='grades'),
]