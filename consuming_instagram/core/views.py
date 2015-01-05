# coding: utf-8
from django.shortcuts import render
from consuming_instagram.core.responses import *


def home(request):
    context = {
        'users': all_users(), 'num_responses': num_responses(), }
    return render(request, 'core/graph.html', context)
