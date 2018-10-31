from django.shortcuts import render
from django.views.generic import View, TemplateView
import subprocess
import sys

# Create your views here.
class IndexView(TemplateView):
    template_name = 'aviation/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
        context['injectme'] = installed_packages
        context['title_text'] = 'AviationVR'
        return context
