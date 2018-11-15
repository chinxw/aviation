from django.shortcuts import render

title_text = "AviationVR"
template_name = 'aviation/index.html'

def index(request):
    if 'zid' in request.session:
        context = {
            'title_text' : request.session['hello'],
            # 'title_text' : title_text,
            'manual_literoomjs' : 'js/LITEroomJS/LITEroom_0.37Beta.js',
        }
        return render(request, template_name, context)
    else:
        return render(request, 'denied.html')
