from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import Report

menu = ['Вводная часть', 'Норматив', 'Фото и измерения', 'Выводы и рекомендации']


def index_report(request):
    reports = Report.objects.all()
    return render(request, 'report/base_r.html', {'reports':reports,'title': 'Tonal', 'menu': menu})


def report_cat(request, cat_id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h2> Категории отчетов </h2><p style=color:red>{cat_id}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)
    return HttpResponse(f'<h1> Архив по годам </h1> <p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')


handler404 = pageNotFound
