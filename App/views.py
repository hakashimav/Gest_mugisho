from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('index2.html')
    return HttpResponse(template.render(context, request))


def datatable(request):
    context = {}
    template = loader.get_template('datatable.html')
    return HttpResponse(template.render(context, request))



def forms(request):
    context = {}
    template = loader.get_template('forms.html')
    return HttpResponse(template.render(context, request))