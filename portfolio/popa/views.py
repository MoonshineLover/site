from django.shortcuts import render
from .models import Counter


# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, Http404


def MainPage(request):
    return render(request, 'popa/MainPage.html')


def sanya(request):
    counter = Counter.objects.first()
    if not counter:
        counter = Counter.objects.create()
    if request.method == 'POST':
        counter.count += 1
        counter.save()
    return render(request, 'popa/sanya.html', {'counter': counter.count})


def what(request, user_id):
    if user_id >999: raise Http404()
    return HttpResponse(f'<h1>ХУУУУУУУУУУУУУУУУУУУУУУУЙ номер {user_id}</h1>')


def pageNotFound(request, exception):
    return render(request, 'error404.html')

def ServerError500(request):
    return render(request, 'error500.html')
