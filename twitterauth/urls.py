from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('twitterauth.views',
    url(r'^info/?$', 'info', name='twitterauth_info'),
    url(r'^login/?$', 'login', name='twitterauth_login'),
    url(r'^login/callback/?$', 'callback', name='twitterauth_callback'),
    url(r'^logout/?$', 'logout', name='twitterauth_logout'),
)
