from django.shortcuts import render
from aviation import views
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.
post_data = {}

@csrf_exempt
def store_to_session(post, msg):
    global post_data
    post_data = post

def redirect_to_app(request):
    request.session['custom_project'] = post_data['custom_project']
    request.session['ext_user_username'] = post_data['ext_user_username']
    return redirect('/'+request.session['custom_project'])
    
    # print("args")
    # request = kwargs.pop('request', None)
    # print(kwargs.get('request'))
    # lr = LTI_redirect()
    # request.session['project'] = post['custom_project']
    # print(post['custom_project'])
    #store into session
    # print(post_data)
    # request.session = post_data


    # if post['custom_project'] == 'aviation':
    #     print(" ")

# class LTI_redirect():
#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request', None)
#         super(LTI_redirect, self).__init__(*args, **kwargs)

    # @csrf_exempt
    # def redirect_to_app(post, msg):
    #     self.request.session['project'] = post['custom_project']
    #     # print(post['custom_project'])
    #     #store into session
    #     if post['custom_project'] == 'aviation':
    #         print(" ")
            # return HttpResponseRedirect(post['custom_project'] + "/")
            # return redirect("/" + post['custom_project'] + "/")
            # context = {
            #     'title_text' : 'AviatiosnVR'
            # }
            # return render(request, 'aviation/index.html', context)
        # views.IndexView.your_view(request)
        # if request.method == "POST":
        #     context = {
        #         'title_text' : 'AviatiosnVR'
        #     }
        #     return render(request, 'aviation/index.html', context)
