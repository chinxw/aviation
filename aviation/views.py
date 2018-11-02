from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
from lti_redirect import views

import subprocess
import sys

title_text = "AviationVR"
template_name = 'aviation/index.html'

# Create your views here.
class IndexView(TemplateView):
    def your_view(request):
        if 'ext_user_username' in request.session:
            context = {
                'title_text' : title_text
            }
            return render(request, template_name, context)
        else:
            return render(request, 'denied.html')

        # print(views.post_data)
        # print("hello")
        # for key, value in request.session.items():
            # print('{} => {}'.format(key, value))
        # print(request.session['ext_user_username'])




        # if request.method == "POST":
        #     for key in request.POST:
        #         print(key)
        #         value = request.POST[key]
        #         print(value)
        # else:

        # if request.method == "POST":
        #     # print(request.consumers)
        #     template = loader.get_template(template_name)
        #     context = {
        #         'title_text' : 'AviatiosnVR'
        #     }
        #     return HttpResponse(template.render(context, request))
        # else:
        #     return render(request, 'denied.html')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    #     installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    #     context['injectme'] = installed_packages
    #     context['title_text'] = 'AviationVR'
    #     return context
