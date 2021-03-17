from django.http import HttpResponse
from django.views.generic.base import TemplateView


def HomePageView(TemplateView):

    template_name = 'task_manager\home_page.html'

def index(request):
    return HttpResponse('Hello')
