from django.http.response import HttpResponse
from django.shortcuts import render


def home(request):
    name='bob'


    return render (request, 'home.html', {'name':name})