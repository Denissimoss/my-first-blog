from django.shortcuts import render
from django.http import HttpResponse
from .models import UserCreationForm
from .models import TableBase
from django.views.generic import ListView
from django.contrib.auth.models import User

 
# Create your views here.
def registr(request):
    return render(request, "pages/registr.html")
# Подключение для рендера
from django.shortcuts import render
# Подключение стандартной формы для регистрации
from django.contrib.auth.forms import UserCreationForm
 
 
# Функция регистрации
def regist(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = UserCreationForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return render(request, 'pages/registr.html', data)
    else: # Иначе
        # Создаём форму
        form = UserCreationForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'pages/registr.html', data)