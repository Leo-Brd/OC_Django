from django.shortcuts import render

from django.http import HttpResponse


def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<ul><li><article>Article 1</article></li><li><article>Article 2</article></li><li><article>Article 3</article></li></ul>')

def contactUs(request):
    return HttpResponse('<h1>Formulaire de contact</h1><form></form>')