from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('socialauth.views',
    url(r'^$', 'index', name = 'socialauth'),
    url(r'^profile$', 'profile', name = 'socialauth_profile'),
    url(r'^twitter/connect/?$', 'twitter_connect', 
        name = 'socialauth_twitter_connect'),
    url(r'^twitter/connect/done/?$', 'twitter_connect_done', 
        name = 'socialauth_twitter_connect_done'),
    url(r'^facebook/connect/?$', 'facebook_connect', 
        name = 'socialauth_facebook_connect'),
    url(r'^facebook/connect/done/?$', 'facebook_connect_done', 
        name = 'socialauth_facebook_connect_done'),
)
