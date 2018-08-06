from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello, world. Burraq Marketing.")


class indexView(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        return render(request,self.template_name)