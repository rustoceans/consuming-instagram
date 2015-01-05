# coding: utf-8
from consuming_instagram.core.responses import *
from django.template.response import TemplateResponse
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def consuming(request):
    context = {}
    response = TemplateResponse(request, 'core/graph.html', context)
    variables = 'all_users cat_users dog_users other_users'.split()
    # simple condition...
    if not 'all_users' in request.COOKIES:
        data_to_graph = [x for x in consuming_instagram()]
        for x in range(len(variables)):
            response.set_cookie(variables[x], data_to_graph[x])
            context[variables[x]] = data_to_graph[x]
    else:
        for x in variables:
            context[x] = request.COOKIES[x]
    print context
    return response
