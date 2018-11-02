"""immersivetech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aviation import views as AviationView
from lti_redirect import views as LTIredirectView
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aviation', AviationView.IndexView.your_view, name="aviation"),
    path('lti/', include('django_lti_auth.urls')),
    path('lti_redirect/', LTIredirectView.redirect_to_app, name="lti_redirect"),
]
