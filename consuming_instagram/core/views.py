# coding: utf-8
from django.shortcuts import render
from consuming_instagram.core.responses import *


# Url default for initialize the loop.
url_default = 'https://api.instagram.com/v1/tags/pets/media/recent?access_token={access_token}'.format(
    access_token=access_token)


def home(request):
    initial_data = get_response(url_default)
    context = {
        'users': get_users_responses(), 'num_responses': num_responses(), }
    return render(request, 'core/base.html', context)
