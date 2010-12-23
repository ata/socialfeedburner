from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from socialauth.decorators import need_profile

@need_profile
def index(request):
    return render_to_response('newsfeed/index.html',{'user': request.user})

@need_profile
def newest(request):
    return HttpResponse('index')
    
@need_profile
def older(request):
    return HttpResponse('index')
