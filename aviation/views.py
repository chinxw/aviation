from django.shortcuts import render

title_text = "AviationVR"
template_name = 'aviation/index.html'

def index(request):
    if 'ext_user_username' in request.session:
        context = {
            'title_text' : title_text,
            'manual_literoomjs' : 'js/LITEroomJS/LITEroom_0.37Beta.js',
        }
        return render(request, template_name, context)
    else:
        return render(request, 'denied.html')
