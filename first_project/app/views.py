from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


WORK_DIR = "work_dir/"


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files = os.listdir(WORK_DIR)
    msg = "Список файлов рабочего каталога:\n\r"
    for number, file in enumerate(files, 1):
        msg = f"{msg}{number}) {file}\n\r"
    return HttpResponse(msg)
