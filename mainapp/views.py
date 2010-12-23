from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render_to_response('mainapp/index.html')

@login_required
def newest(request):
    return HttpResponse('index')
    
@login_required
def older(request):
    return HttpResponse('index')
    
@login_required
def connect(request):
    return HttpResponse('index')
