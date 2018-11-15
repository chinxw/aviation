from django.shortcuts import render
from aviation import views
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from passlib.hash import pbkdf2_sha256
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
# import logging

# log = logging.getLogger(__name__)

@csrf_exempt
def store_to_session(post, request):
    roles = post["roles"].split(";")
    role_mappings = {
        'staff': ['Instructor'],
        'student': ['Student']
    }
    role = "STAFF" if any(filter(lambda role: role in role_mappings['staff'], roles)) else "STUDENT"
    request.session['role'] = role
    request.session['zid'] = post['ext_user_username']
    request.session['given_name'] = post['lis_person_name_given']
    request.session['family_name'] = post['lis_person_name_family']
    request.session['full_name'] = post['lis_person_name_full']
    request.session['email'] = post['lis_person_contact_email_primary']
    request.session['return_url'] = post['launch_presentation_return_url']
    request.session['custom_project'] = post['custom_project']
    first_name = request.session['given_name'][0]
    last_name = request.session['family_name'][0]
    email = request.session['email'][0]
    password = pbkdf2_sha256.using(salt=bytes(settings.SECRET_KEY, encoding="UTF-8")).hash(email)
    request.session.set_expiry(30*60)

    User = get_user_model()
    try:
        user = authenticate(username=email, password=password)
        request.session['hello'] = 'Authenticated' 
    except (ValueError, User.DoesNotExist):
        user = User.objects.create_user(
            username=email, email=email, password=password, first_name=first_name, last_name=last_name
        )
        if role == "STAFF":
            user.is_staff = True
        user.save()
        request.session['hello'] = 'NOT AUTHENTICATED' 

def redirect_to_app(request):
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
