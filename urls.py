from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

admin.autodiscover()

js_info_dict = {
    'packages': ('newsfeed',),
}


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^login/?$', 'django.contrib.auth.views.login',{
        'authentication_form': AuthenticationForm,
        #'next': '/',
        'template_name': 'login.html',}),
    (r'^logout/?$', 'django.contrib.auth.views.logout',
        {'next_page': '/',}),
    (r'^newest/(?P<after>\w+)/?$','newsfeed.views.newest'),
    (r'^older/(?P<before>\w+)/?$','newsfeed.views.older'),
    (r'^newsfeed/',include('newsfeed.urls')),
    (r'^socialauth/',include('socialauth.urls')),
    (r'^twitterauth/',include('twitterauth.urls')),
    (r'^$','newsfeed.views.index'),
)
