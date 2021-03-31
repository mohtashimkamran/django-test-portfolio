from django.shortcuts import render ,  HttpResponse
from django.conf import settings
# Create your views here.

def index(request):
    context={
        'name' : settings.DATA['NAME'],
        'intro' : settings.DATA['intro'],
        'about_me' : settings.DATA['ABOUT_ME'],
        'projects' : settings.DATA['PROJECT'],
        'languages' : settings.DATA['LANGUAGES'],

    }
    return render(request,'main\index.html',context)