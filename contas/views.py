from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    #html = "<html><body>Its now %s.</body></html>" % now
    return render(request, 'home.hmtl')