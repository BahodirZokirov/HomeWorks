from django.urls import path
from .views import themes

urlpatterns = [
    path("", themes, name='mavzular'),
]