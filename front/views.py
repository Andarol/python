from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_node_apps(request):
    return HttpResponse('hello from Notes app'.encode(), status=HTTPStatus.OK)


def new_page(request):
    return render(request, 'index.html')
    return HttpResponse('hello from Notes app'.encode(), status=HTTPStatus.OK)
