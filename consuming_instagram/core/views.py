# coding: utf-8
from django.shortcuts import render
from consuming_instagram.core.responses import *


def home(request):
    print num_responses()
    context = {'users': get_responses(), }
    return render(request, 'core/base.html', context)
