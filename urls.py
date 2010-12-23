from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm

admin.autodiscover()

js_info_dict = {
    'packages': ('mainapp',),
}


urlpatterns = patterns('',
    (r'^$','mainapp.views.index'),
    (r'^newest/(?P<after>\w+)$','mainapp.views.newest'),
    (r'^older/(?P<before>\w+)$','mainapp.views.older'),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^login/$', 'django.contrib.auth.views.login',
        {'authentication_form': AuthenticationForm,
        #'next': '/',
        'template_name': 'login.html',}),
    (r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/',}),
    #(r'^jsi18n/$', 'django.views.i18n.javascript_catalog',js_info_dict),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
