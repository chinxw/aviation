from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'aviation/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'oaiuhsdfaijksdfgh AAAAA'
        context['title_text'] = 'AviationVR'
        return context
