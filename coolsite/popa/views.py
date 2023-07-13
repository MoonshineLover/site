from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, Http404


def main_page(request):
    return HttpResponse('<h1>Страница найдена ошибки 404 не буде</h1>')


def sanya(request):
    return HttpResponse('<h1>саня соси хуй</h1>')


def index(request):
    return HttpResponse(f'эта траницатоже найдена но ошибка 404 буде (потом)')


def what(request, user_id):
    if user_id >999: raise Http404()
    return HttpResponse(f'<h1>ХУУУУУУУУУУУУУУУУУУУУУУУЙ номер {user_id}</h1>')


def pageNotFound(request, exception):
    return render(request, 'popa/error404.html')

def ServerError500(request):
    return render(request, 'popa/error500.html')