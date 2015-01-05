# coding: utf-8
from consuming_instagram.core.responses import *
from django.template.response import TemplateResponse


def consuming(request):
    context = {}
    response = TemplateResponse(request, 'core/graph.html', context)
    if not 'all_users' in request.COOKIES:
        users = consuming_instagram()[0]
        response.set_cookie('all_users', users)
        context['all_users'] = users
        context['teste'] = 'EUUUU'
    else:
        context['all_users'] = request.COOKIES['all_users']
    print context
    return response
