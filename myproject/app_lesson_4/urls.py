from django.urls import path
from app_lesson_4.views import lesson_4_view

app_name = 'app_lesson_4'

urlpatterns = [
    path('', lesson_4_view, name='lesson_4'),
]
