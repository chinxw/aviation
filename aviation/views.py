from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader

import subprocess
import sys

template_name = 'aviation/index.html'

# Create your views here.
class IndexView(TemplateView):
    @csrf_exempt
    def your_view(request):
        if request.method == "POST":
            # print(request.consumers)
            template = loader.get_template(template_name)
            context = {
                'title_text' : 'AviationVR'
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse("Sorry your not allowed")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
        context['injectme'] = installed_packages
        context['title_text'] = 'AviationVR'
        return context
